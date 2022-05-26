import pygame as p
from pygame import Surface
from .images_helpers import scale_image, load_image
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

floor_surface: Surface = load_image("Sprites", "floor.png")

FLOOR: Surface = scale_image(floor_surface, (floor_surface.get_width() * 4, floor_surface.get_height() * 4))

(FLOOR_WIDTH, FLOOR_HEIGHT) = FLOOR.get_size()

FLOOR_POSITION = (SCREEN_WIDTH/2, SCREEN_HEIGHT - FLOOR.get_height()/2)


# Define class for Floor

class Floor(p.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = FLOOR
        self.rect = self.image.get_rect()
        self.rect.center = FLOOR_POSITION
