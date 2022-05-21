import pygame as p
from pygame import Surface
from .images_helpers import scale_image, load_image
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

floor_surface: Surface = load_image("Sprites", "floor.png")

FLOOR: Surface = scale_image(floor_surface, (SCREEN_WIDTH, floor_surface.get_height() * 10))

(FLOOR_WIDTH, FLOOR_HEIGHT) = FLOOR.get_size()

FLOOR_POSITION = (SCREEN_WIDTH/2, SCREEN_HEIGHT - FLOOR.get_height()/2)


# Define class for Floor

class Floor(p.sprite.Sprite):
    def __init__(self, floor: Surface) -> None:
        super().__init__()
        self.image = floor
        self.rect = self.image.get_rect()
        self.rect.center = FLOOR_POSITION
