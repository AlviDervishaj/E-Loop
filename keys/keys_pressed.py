# DECIDE WHAT TO DO WITH CERTAIN KEY PRESSES
from pygame import K_LEFT, K_RIGHT, K_a, K_d
from constants import VELOCITY, SCREEN_WIDTH
from helpers import character_hit_box


# handle character movement here
def character_movement(keys):
    # move character right as long as it is on screen
    if (keys[K_a] or keys[K_LEFT]) and character_hit_box.x - VELOCITY > 0:
        character_hit_box.x -= VELOCITY
    # move character left as long as it is on screen
    elif (keys[K_d] or keys[K_RIGHT]) and character_hit_box.x + VELOCITY + character_hit_box.width < SCREEN_WIDTH:
        character_hit_box.x += VELOCITY
