from constants import SCREEN_HEIGHT, SCREEN_WIDTH, VELOCITY, SURFACE
from .images_helpers import flip_image_x, scale_image, load_image
from .floor_helpers import FLOOR_HEIGHT
from pygame import K_LEFT, K_RIGHT, K_SLASH, K_a, K_d, K_e, Surface, sprite, key, draw

# load all sprites for walk animation
char_walk = [
    load_image("Char_Animation_Right", "Char1.png"), load_image(
        "Char_Animation_Right", "Char2.png"),
    load_image("Char_Animation_Right", "Char3.png"), load_image(
        "Char_Animation_Right", "Char4.png"),
    load_image("Char_Animation_Right", "Char5.png"), load_image(
        "Char_Animation_Right", "Char6.png"),
    load_image("Char_Animation_Right", "Char7.png"), load_image(
        "Char_Animation_Right", "Char8.png"),
    load_image("Char_Animation_Right", "Char9.png"), load_image(
        "Char_Animation_Right", "Char10.png")
]

# load still image and scale it
char_still = load_image("Char_Still", "Still0.png")
char_still_scaled = scale_image(char_still, (char_still.get_width()*4, char_still.get_height()*4 ))

# scale all walk animation images
char_walk_scaled = [
    scale_image(char_walk[0], (char_still.get_width()*4, char_still.get_height()*4 )), scale_image(
        char_walk[1], (char_still.get_width()*4,  char_still.get_height()*4)),
    scale_image(char_walk[2], (char_still.get_width()*4,  char_still.get_height()*4)), scale_image(
        char_walk[3], (char_still.get_width()*4,  char_still.get_height()*4)),
    scale_image(char_walk[4], (char_still.get_width()*4,  char_still.get_height()*4)), scale_image(
        char_walk[5], (char_still.get_width()*4,  char_still.get_height()*4)),
    scale_image(char_walk[6], (char_still.get_width()*4,  char_still.get_height()*4)), scale_image(
        char_walk[7], (char_still.get_width()*4,  char_still.get_height()*4)),
    scale_image(char_walk[8], (char_still.get_width()*4,  char_still.get_height()*4)), scale_image(
        char_walk[9], (char_still.get_width()*4,  char_still.get_height()*4))
]

# Get size of one sprite
(CHARACTER_WIDTH, CHARACTER_HEIGHT) = char_walk_scaled[0].get_size()

CHARACTER_X = SCREEN_WIDTH / 2
CHARACTER_Y = SCREEN_HEIGHT - FLOOR_HEIGHT - CHARACTER_HEIGHT/2 + 12 #+12 per pjesen transparente lart plus q tduklet sikur esht nmes tbarit


# Defining class for our character
class Character(sprite.Sprite):
    def __init__(self, char_walking: list, char_standing: Surface) -> None:
        super().__init__()
        self.animation = char_walking
        self.still = char_standing
        self.image = self.still
        self.rect = self.image.get_rect()
        self.rect.center = [CHARACTER_X, CHARACTER_Y]
        self.hitbox = self.rect.inflate(-30,0)
        self.left = False
        self.right = False
        self.walk_count = 0


        # Is a unit for how many shields we can activate
        self.energy = 3

    # update function to handle movement
    def update(self) -> None:
        keys = key.get_pressed()
        self.handle_movement(keys)
        if self.right:
            self.walk_count += 1
            if self.walk_count // 3 >= 10:
                self.walk_count = 0
            self.image = self.animation[self.walk_count // 3]
        elif self.left:
            self.walk_count += 1
            if self.walk_count // 3 >= 10:
                self.walk_count = 0
            self.image = flip_image_x(self.animation[self.walk_count // 3])
        elif not self.left and not self.right:
            self.image = self.still
        
        # Hitbox Purposes only
        draw.rect(SURFACE,(255,0,0), self.rect, 2)

    def handle_movement(self, keys) -> None:
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
            self.walk_count = 0

    # A function that returns the position of the character
    def pos(self) -> tuple:
        return (self.rect.centerx, self.rect.centery)

    # Creates new shield when the conditions are met
    def enable_shield(self, shield_group) -> bool:
        if self.energy > 0 and len(shield_group) < 1:
            self.energy -= 1
            return True
        else:
            return False
