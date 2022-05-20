# DECIDE WHAT TO DO WITH CERTAIN KEY PRESSES
from pygame import K_a, K_d
from constants import VELOCITY, SCREEN_WIDTH
from helpers import character_hit_box, blit_surface


# handle character movement here
def character_movement(keys):
    # move character right as long as it is on screen
    if keys[K_a] and character_hit_box.x - VELOCITY > 0:
        character_hit_box.x -= VELOCITY
    # move character left as long as it is on screen
    elif keys[K_d] and character_hit_box.x + VELOCITY + character_hit_box.width < SCREEN_WIDTH:
        character_hit_box.x += VELOCITY
