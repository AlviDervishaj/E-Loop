from pygame import init, quit, time, event, QUIT, KEYDOWN, K_r, K_ESCAPE
from constants.constants import BOMB_MAX, BOMB_TIME, SURFACE
from helpers import draw_border, bomb_group, character_group, floor_group, background_group, collision_detect, bomb_spawn
from constants import DISPLAY, FPS

# initialize game functions


def handle_game_start() -> None:
    init()


def quit_game() -> None:
    quit()


def draw_window() -> None:
    # update entire display every time function is called
    DISPLAY.flip()
    # draw border around window
    draw_border()
    # draw all our sprite groups in order
    background_group.draw(SURFACE)
    floor_group.draw(SURFACE)
    bomb_group.draw(SURFACE)
    character_group.draw(SURFACE)
    # call update function of character class
    character_group.update()
    bomb_group.update()


# main function that will run once file is executed ( run )
def main() -> None:
    handle_game_start()
    clock = time.Clock()
    bomb_timer = 0

    # main loop
    running: bool = True
    while running:
        # control speed of while loop
        # so that the game runs on constant FPS
        clock.tick(FPS)
        for _event_ in event.get():
            if _event_.type == QUIT:
                running = False
                quit_game()
                return
            if _event_.type == KEYDOWN:
                # user has pressed a key which we might user for
                # character movement later
                if _event_.key == K_r:
                    main()
                if _event_.key == K_ESCAPE:
                    run = False
                    quit_game()
                    return
        bomb_timer+= 1
        if len(bomb_group) < BOMB_MAX and bomb_timer >= BOMB_TIME:
            bomb_timer = 0
            new_bomb = bomb_spawn()
            bomb_group.add(new_bomb)
        collision_detect(bomb_group, floor_group, character_group)
        draw_window()


# do not allow this file to run when imported.
# Run only when executed
if __name__ == "__main__":
    # run main function
    main()
