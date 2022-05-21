# DECIDE WHAT TO DO WITH CERTAIN KEY PRESSES
from pygame import K_LEFT, K_RIGHT, K_a, K_d
from constants import VELOCITY, SCREEN_WIDTH


# handle character movement here
def character_movement(keys, self):
    # move character left as long as it is on screen
    if (keys[K_a] or keys[K_LEFT]) and self.rect.x - VELOCITY > 0:
        self.rect.x -= VELOCITY

        # update player direction, used for animation
        self.right = False
        self.left = True

    # move character right as long as it is on screen
    elif (keys[K_d] or keys[K_RIGHT]) and self.rect.x + VELOCITY + self.rect.width < SCREEN_WIDTH:
        self.rect.x += VELOCITY

        # update player direction to left, also for animation
        self.right = True
        self.left = False

    # When player is not moving, used for standing animation
    else:
        self.right = False
        self.left = False
        self.walkcount = 0
