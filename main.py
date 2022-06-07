from pygame import MOUSEBUTTONDOWN, K_e, K_p, init, quit, time, event, QUIT, KEYDOWN, K_r, K_ESCAPE, mouse
from constants import SURFACE, NEW_QUESTION, DEATH
from helpers import draw_border, collision_detect, Shield, Pop_Up, Question
from helpers import handle_bomb_spawn, handle_question_spawn, question_collision_detect
from sprites import background_group, floor_group, bomb_group, shield_group, character_group, character
from sprites import pointer_group, question_drop_group, popup_group, score
from constants import DISPLAY, FPS

# General variables and settings
timepaused = 0
ispaused = False
extratime = 0
isclicked = False
question = False
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
    bomb_group.draw(SURFACE)
    question_drop_group.draw(SURFACE)
    character_group.draw(SURFACE)
    shield_group.draw(SURFACE)
    score.draw()

def update_window() -> None:
    # call update function of character and bomb class
    character_group.update()
    shield_group.update(character.pos(), bomb_group)
    bomb_group.update()
    question_drop_group.update()
    score.update(extratime)

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
        global isclicked
        isclicked = False
        for _event_ in event.get():
            if _event_.type == QUIT:
                # quit game after closing window
                running = False
                quit_game()
                return
            if _event_.type == NEW_QUESTION:
                global question
                if question == False:
                    q = Pop_Up("State your programming knowledge","Beginner","Amateur","Advanced","Expert")
                    popup_group.add(q)
                    question = True
                    pause_game()
                else:
                    question = False
                    pause_game()
            if _event_.type == MOUSEBUTTONDOWN:
                isclicked = True
            if _event_.type == DEATH:
                pause_game()
                game_over = Question("You lost! Score: " + str(score.myscore()))
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
                if _event_.key == K_p:
                    pause_game()

        # Draw everything everytime function is called
        draw_window()
        # If not paused update every group
        if not ispaused:
            handle_bomb_spawn(bomb_group,extratime)
            handle_question_spawn(question_drop_group,extratime)
            collision_detect(bomb_group, floor_group, character_group)
            question_collision_detect(question_drop_group, floor_group, character_group)
            update_window()
        # Draws Pointer even when paused
        if ispaused:
            update_others()

# do not allow this file to run when imported.
# Run only when executed
if __name__ == "__main__":
    # run main function
    main()
