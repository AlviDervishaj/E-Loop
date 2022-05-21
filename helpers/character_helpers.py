import pygame as p
from pygame import Surface
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from keys import character_movement
from .images_helpers import horizontal_image_flip, scale_image, load_image
from .floor_helpers import FLOOR_HEIGHT

# load all sprites for walk animation
char_walk: list = [load_image("Char_Animation_Right", "Char1.png"), load_image("Char_Animation_Right", "Char2.png"), load_image("Char_Animation_Right", "Char3.png"), load_image(
    "Char_Animation_Right", "Char4.png"), load_image("Char_Animation_Right", "Char5.png"), load_image("Char_Animation_Right", "Char6.png"), load_image(
    "Char_Animation_Right", "Char7.png"), load_image("Char_Animation_Right", "Char8.png"), load_image("Char_Animation_Right", "Char9.png"), load_image("Char_Animation_Right", "Char10.png")]

# load still image and scale it
char_still: Surface = load_image("Char_Still","Still0.png")
char_still_scaled: Surface = scale_image(char_still, (105, 135))

# scale all walk animation images
char_walk_scaled: list = [scale_image(char_walk[0], (105, 135)), scale_image(char_walk[1], (105, 135)), scale_image(char_walk[2], (105, 135)), scale_image(char_walk[3], (105, 135)), scale_image(
    char_walk[4], (105, 135)), scale_image(char_walk[5], (105, 135)), scale_image(char_walk[6], (105, 135)), scale_image(char_walk[7], (105, 135)), scale_image(
    char_walk[8], (105, 135)), scale_image(char_walk[9], (105, 135))]

# Get size of one sprite
(CHARACTER_WIDTH, CHARACTER_HEIGHT) = char_walk_scaled[0].get_size()

CHARACTER_X = SCREEN_WIDTH / 2
CHARACTER_Y = SCREEN_HEIGHT - FLOOR_HEIGHT - CHARACTER_HEIGHT/2


# Defining class for our character
class Character(p.sprite.Sprite):
    def __init__(self, char_walking: list, char_standing: Surface) -> None:
        super().__init__()
        self.animation = char_walking
        self.still = char_standing
        self.image = self.still
        self.rect = self.image.get_rect()
        self.rect.center = [CHARACTER_X, CHARACTER_Y]
        self.left = False
        self.right = False
        self.walkcount = 0

    # update function to handle movement
    def update(self) -> None:
        keys = p.key.get_pressed()
        character_movement(keys, self)
        if self.right:
            self.walkcount += 1
            if self.walkcount // 3 >= 10:
                self.walkcount = 0
            self.image = self.animation[self.walkcount//3]
        elif self.left:
            self.walkcount += 1
            if self.walkcount // 3 >= 10:
                self.walkcount = 0
            self.image = horizontal_image_flip(
                self.animation[self.walkcount//3])
        elif not self.left and not self.right:
            self.image = self.still


# Creating character using character class
character = Character(char_walk_scaled, char_still_scaled)
character_group = p.sprite.Group()
character_group.add(character)
