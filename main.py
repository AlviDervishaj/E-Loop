from pygame import Surface, init, quit, time, event, QUIT, KEYDOWN, key
from colors.colors import BACKGROUND
from helpers import fill_surface_with_color, scale_image, blit_surface, draw_border, load_image
from keys import character_movement
from constants import DISPLAY, FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from colors import BLACK


# initialize game functions
def handle_game_start() -> None:
    init()


def quit_game() -> None:
    quit()


def draw_window(floor: Surface, floor_position: tuple, character: Surface, character_position: tuple) -> None:
    draw_border()
    fill_surface_with_color(BACKGROUND)
    # after filling screen black
    # display character
    blit_surface(floor, floor_position)
    blit_surface(character, character_position)
    DISPLAY.update()


# main function that will run once file is executed ( run )
def main() -> None:
    handle_game_start()
    floor_surface: Surface = load_image("floor.png")
    floor_scaled = scale_image(floor_surface, (SCREEN_WIDTH, SCREEN_HEIGHT / 3))

    character_surface: Surface = load_image("character.png")
    character_scaled = scale_image(character_surface, (256, 256))
    DISPLAY.flip()
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
                print(_event_.key)
        # each time loop reaches this line it will tell use which keys
        # are being pressed
        keys_pressed = key.get_pressed()
        # handle key presses for character
        character_movement(keys_pressed)
        draw_window(floor_scaled, (0, SCREEN_HEIGHT - floor_scaled.get_height()), character_scaled
                    , (SCREEN_WIDTH / 2 - character_scaled.get_width() / 2, floor_scaled.get_height()))


# do not allow this file to run when imported.
# Run only when executed
if __name__ == "__main__":
    # run main function
    main()
