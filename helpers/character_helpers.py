from constants import SCREEN_HEIGHT, SCREEN_WIDTH, VELOCITY, SURFACE
from .images_helpers import flip_image_x, scale_image, load_image
from .floor_helpers import FLOOR_HEIGHT
from pygame import K_LEFT, K_RIGHT, K_SLASH, K_a, K_d, K_e, Surface, sprite, key, draw

# load all sprites for walk right animation
char_walk_right = [
    load_image("Char_Animation_Right", "CharR1.png"), load_image(
        "Char_Animation_Right", "CharR2.png"),
    load_image("Char_Animation_Right", "CharR3.png"), load_image(
        "Char_Animation_Right", "CharR4.png"),
    load_image("Char_Animation_Right", "CharR5.png"), load_image(
        "Char_Animation_Right", "CharR6.png")
]

# load all sprites for walk left animation
char_walk_left = [
    load_image("Char_Animation_Left", "CharL1.png"), load_image(
        "Char_Animation_Left", "CharL2.png"),
    load_image("Char_Animation_Left", "CharL3.png"), load_image(
        "Char_Animation_Left", "CharL4.png"),
    load_image("Char_Animation_Left", "CharL5.png"), load_image(
        "Char_Animation_Left", "CharL6.png")
]

# load still image and scale it
char_still = load_image("Char_Still", "Still0.png")
char_still_scaled = scale_image(char_still, (char_still.get_width()*5, char_still.get_height()*5 ))

# scale all walk right animation images
char_walk_right_scaled = [
    scale_image(char_walk_right[0], (char_still.get_width()*5, char_still.get_height()*5 )), scale_image(
        char_walk_right[1], (char_still.get_width()*5,  char_still.get_height()*5)),
    scale_image(char_walk_right[2], (char_still.get_width()*5,  char_still.get_height()*5)), scale_image(
        char_walk_right[3], (char_still.get_width()*5,  char_still.get_height()*5)),
    scale_image(char_walk_right[4], (char_still.get_width()*5,  char_still.get_height()*5)), scale_image(
        char_walk_right[5], (char_still.get_width()*5,  char_still.get_height()*5))
]

# scale all walk left animation images
char_walk_left_scaled = [
    scale_image(char_walk_left[0], (char_still.get_width()*5, char_still.get_height()*5 )), scale_image(
        char_walk_left[1], (char_still.get_width()*5,  char_still.get_height()*5)),
    scale_image(char_walk_left[2], (char_still.get_width()*5,  char_still.get_height()*5)), scale_image(
        char_walk_left[3], (char_still.get_width()*5,  char_still.get_height()*5)),
    scale_image(char_walk_left[4], (char_still.get_width()*5,  char_still.get_height()*5)), scale_image(
        char_walk_left[5], (char_still.get_width()*5,  char_still.get_height()*5))
]

# Get size of one sprite
(CHARACTER_WIDTH, CHARACTER_HEIGHT) = char_walk_right_scaled[0].get_size()

CHARACTER_X = SCREEN_WIDTH / 2
CHARACTER_Y = SCREEN_HEIGHT - FLOOR_HEIGHT - CHARACTER_HEIGHT/2 + 12 #+12 per pjesen transparente lart plus q tduklet sikur esht nmes tbarit


# Defining class for our character
class Character(sprite.Sprite):
    def __init__(self, char_right: list, char_left: list, char_standing: Surface) -> None:
        super().__init__()
        self.walkright = char_right
        self.walkleft = char_left
        self.still = char_standing
        self.image = self.still
        self.rect = self.image.get_rect()
        self.rect.center = [CHARACTER_X, CHARACTER_Y]
        self.hitbox = self.rect.inflate(-30,0)
        self.left = False
        self.right = False
        self.walk_count = 0

        # Is a unit for how many shields we can activate
        self.energy = 0

    # update function to handle movement
    def update(self) -> None:
        keys = key.get_pressed()
        self.handle_movement(keys)
        if self.right:
            self.walk_count += 1
            if self.walk_count // 4 >= 6:
                self.walk_count = 0
            self.image = self.walkright[self.walk_count // 4]
        elif self.left:
            self.walk_count += 1
            if self.walk_count // 4 >= 6:
                self.walk_count = 0
            self.image = self.walkleft[self.walk_count // 4]
        elif not self.left and not self.right:
            self.image = self.still
        
        # Hitbox Purposes only
        #draw.rect(SURFACE, (255, 0, 0), self.rect, 2)

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
        return self.rect.centerx, self.rect.centery

    # Creates new shield when the conditions are met
    def enable_shield(self, shield_group) -> bool:
        if self.energy > 0 and len(shield_group) < 1:
            self.energy -= 1
            return True
        else:
            return False
    def add_shield(self) -> None:
        self.energy+=1