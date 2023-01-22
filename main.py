from pygame import MOUSEBUTTONDOWN, K_e, K_p, init, quit, time, event, QUIT, KEYDOWN, K_r, K_q, K_ESCAPE, mouse
from constants import SURFACE, NEW_QUESTION, DEATH, PLAYER_DAMAGE, ADDHEALTH, ADDSHIELD, ADDTURRET
from helpers import draw_border, collision_detect, Shield, Pop_Up, Question, turretGroup, turretdisplaygroup
from helpers import spawnTurret, dropSpawn, dropGroup, question_collision_detect, wave_handler
from sprites import background_group, floor_group, bomb_group, shield_group, character_group, character
from sprites import pointer_group, question_drop_group, popup_group, score, HUD_object
from constants import DISPLAY, FPS

# General variables and settings
timepaused = 0
ispaused = False
extratime = 0
isclicked = False
question = False
durability = 0
# initialize game functions


def handle_game_start() -> None:
    init()
    mouse.set_visible(False)


def quit_game() -> None:
    quit()


def pause_game() -> None:
    global ispaused, timepaused, extratime
    if ispaused is True:
        ispaused = False
        new_time = time.get_ticks()
        extratime = new_time - timepaused
    else:
        ispaused = True
        timepaused = time.get_ticks()


def update_others() -> None:
    # Draws others
    popup_group.draw(SURFACE)
    popup_group.update(isclicked)
    pointer_group.draw(SURFACE)
    pointer_group.update()


def draw_window() -> None:
    # update entire display
    DISPLAY.flip()
    # draw border around window
    draw_border()
    # draw all our sprite groups in order
    background_group.draw(SURFACE)
    floor_group.draw(SURFACE)
    turretGroup.draw(SURFACE)
    # question_drop_group.draw(SURFACE)
    dropGroup.draw(SURFACE)
    bomb_group.draw(SURFACE)
    character_group.draw(SURFACE)
    shield_group.draw(SURFACE)
    score.draw()
    HUD_object.draw()
    turretdisplaygroup.draw(SURFACE)
    HUD_object.draw_health(character.get_health())


def update_window() -> None:
    # call update function of character and bomb class
    character_group.update()
    shield_group.update(character.pos(), bomb_group)
    bomb_group.update()
    turretGroup.update(bomb_group, dropGroup)
    # question_drop_group.update(floor_group)
    dropGroup.update(floor_group, character_group)
    score.update(extratime)
    turretdisplaygroup.update(character.turretAmount)
    HUD_object.update(durability, shield_group, character.get_shield_amount())

# main function that will run once file is executed ( run )


def main() -> None:
    handle_game_start()
    clock = time.Clock()

    # main loop
    running: bool = True

    while running:
        # control speed of while loop
        # so that the game runs on constant FPS
        clock.tick(FPS)
        global isclicked, durability
        isclicked = False
        if len(shield_group) > 0:
            durability = new_shield.get_durability()
        for _event_ in event.get():
            if _event_.type == QUIT:
                # quit game after closing window
                running = False
                quit_game()
                return
            if _event_.type == NEW_QUESTION:
                global question
                if question == False:
                    q = Pop_Up("State your programming knowledge",
                               "Beginner", "Amateur", "Advanced", "Expert")
                    popup_group.add(q)
                    question = True
                    pause_game()
                else:
                    question = False
                    pause_game()
                    character.add_shield()
            if _event_.type == PLAYER_DAMAGE:
                character.damage()
            if _event_.type == ADDHEALTH:
                if (character.get_health() < 16):
                    character.add_health()
            if _event_.type == ADDSHIELD:
                character.add_shield()

            if _event_.type == ADDTURRET:
                character.add_turret()

            if _event_.type == MOUSEBUTTONDOWN:
                isclicked = True

            if _event_.type == DEATH:
                pause_game()
                game_over = Question(
                    "You lost! Score: " + str(score.myscore()))
                popup_group.add(game_over)

            if _event_.type == KEYDOWN:
                # user has pressed a key which we might user for
                # character movement later
                if _event_.key == K_r:
                    # restart game
                    main()
                if _event_.key == K_ESCAPE:
                    # quit game
                    running = False
                    quit_game()
                    return
                if _event_.key == K_e:
                    # give character shield
                    if character.enable_shield(shield_group):
                        pos = character.pos()
                        new_shield = Shield(pos)
                        shield_group.add(new_shield)
                if _event_.key == K_q:
                    if character.energy > 0 and character.turretAmount > 0:
                        character.energy -= 1
                        character.turretAmount -= 1
                        spawnTurret(character.pos())
                # Developer purposes only
                # if _event_.key == K_p:
                    # pause_game()

        # Draw everything everytime function is called
        draw_window()
        # If not paused update every group
        if not ispaused:
            # handle_bomb_wave(bomb_group, extratime)
            wave_handler()
            # handle_question_spawn(question_drop_group, extratime)
            dropSpawn()
            collision_detect(bomb_group, floor_group, character_group)
            # question_collision_detect(question_drop_group, character_group)
            update_window()
        # Draws Pointer even when paused
        if ispaused:
            update_others()


# do not allow this file to run when imported.
# Run only when executed
if __name__ == "__main__":
    # run main function
    main()
