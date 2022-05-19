# DECIDE WHAT TO DO WITH CERTAIN KEY PRESSES
from pygame import K_a, K_d, K_w, K_s
from constants import VELOCITY, SCREEN_HEIGHT, SCREEN_WIDTH
from helpers import character_hit_box


# handle character movement here
def character_movement(keys):
    # move character right as long as it is on screen
    if keys[K_a] and character_hit_box.x - VELOCITY > 0:
        character_hit_box.x -= VELOCITY
    # move character left as long as it is on screen
    elif keys[K_d] and character_hit_box.x + VELOCITY + character_hit_box.width < SCREEN_WIDTH:
        character_hit_box.x += VELOCITY
    # move character down as long as it is on screen
    elif keys[K_s] and character_hit_box.y + VELOCITY + character_hit_box.width < SCREEN_HEIGHT:
        character_hit_box.y += VELOCITY
    # Move character up
    # as long as it is inside screen
    elif keys[K_w] and character_hit_box.y - VELOCITY > 0:
        character_hit_box.y -= VELOCITY
