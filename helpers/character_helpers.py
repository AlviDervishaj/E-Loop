import pygame as p
from pygame import K_LEFT, K_RIGHT, K_a, K_d, Surface, Rect
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, VELOCITY
from .images_helpers import scale_image, load_image
from .floor_helpers import FLOOR_HEIGHT

# load image
character_surface: Surface = load_image("CharacterTransparent.png")

CHARACTER: Surface = scale_image(character_surface, (112, 88))
(CHARACTER_WIDTH, CHARACTER_HEIGHT) = CHARACTER.get_size()

CHARACTER_X = SCREEN_WIDTH / 2
CHARACTER_Y = SCREEN_HEIGHT - FLOOR_HEIGHT - CHARACTER_HEIGHT/2

# Defining class for our character


class Character(p.sprite.Sprite):
    def __init__(self, char: Surface) -> None:
        super().__init__()
        self.image = char
        self.rect = self.image.get_rect()
        self.rect.center = [CHARACTER_X, CHARACTER_Y]

    def update(self) -> None:
        keys = p.key.get_pressed()
        # move character right as long as it is on screen
        if (keys[K_a] or keys[K_LEFT]) and self.rect.x - VELOCITY > 0:
            self.rect.x -= VELOCITY
        # move character left as long as it is on screen
        elif (keys[K_d] or keys[K_RIGHT]) and self.rect.x + VELOCITY + self.rect.width < SCREEN_WIDTH:
            self.rect.x += VELOCITY


# Creating character using character class
character = Character(CHARACTER)
character_group = p.sprite.Group()
character_group.add(character)
