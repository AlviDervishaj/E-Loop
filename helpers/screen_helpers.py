import pygame as p
from pygame import Surface, draw
from constants import SURFACE, BORDER, SCREEN_HEIGHT, SCREEN_WIDTH
from .images_helpers import load_image, scale_image
from colors import BLACK


def fill_surface_with_color(color: tuple) -> None:
    SURFACE.fill(color)


def blit_surface(obj: Surface, coordinates: tuple) -> None:
    SURFACE.blit(obj, coordinates)


def draw_border() -> None:
    draw.rect(SURFACE, BLACK, BORDER)


#Get background image and scale it
background_surface: Surface = load_image("space.png")
BACKGROUND: Surface = scale_image(background_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND_POSITION = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

#Define Background Class for bg
class Background(p.sprite.Sprite):
    def __init__(self, bg: Surface) -> None:
        super().__init__()
        self.image = bg
        self.rect = self.image.get_rect()
        self.rect.center = BACKGROUND_POSITION

#Create background from class
background = Background(BACKGROUND)
#Create new group for background
background_group = p.sprite.Group()
background_group.add(background)