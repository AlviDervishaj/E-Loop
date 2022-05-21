from pygame import init, quit, time, event, QUIT, KEYDOWN, key, K_r, K_ESCAPE
from helpers import blit_surface, draw_border, FLOOR, FLOOR_POSITION,\
   CHARACTER, character_hit_box, fill_surface_with_color
from keys import character_movement
from constants import DISPLAY, FPS
from colors import WHITE


# initialize game functions
def handle_game_start() -> None:
    init()


def quit_game() -> None:
    quit()


def draw_window() -> None:
    draw_border()
    fill_surface_with_color(WHITE)
    # after filling screen black
    # display character
    blit_surface(FLOOR, FLOOR_POSITION)
    blit_surface(CHARACTER, (character_hit_box.x, character_hit_box.y))
    DISPLAY.update()


# main function that will run once file is executed ( run )
def main() -> None:
    handle_game_start()
    DISPLAY.update()
    clock = time.Clock()
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
        # each time loop reaches this line it will tell use which keys
        # are being pressed
        keys_pressed = key.get_pressed()
        # handle key presses for character
        character_movement(keys_pressed)
        draw_window()


# do not allow this file to run when imported.
# Run only when executed
if __name__ == "__main__":
    # run main function
    main()
