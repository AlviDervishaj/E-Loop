from pygame import Surface, draw, sprite
from constants import SURFACE, BORDER, SCREEN_HEIGHT, SCREEN_WIDTH
from .images_helpers import load_image, scale_image
from colors import BLACK


def fill_surface_with_color(color: tuple) -> None:
    SURFACE.fill(color)


def blit_surface(obj: Surface, coordinates: tuple) -> None:
    SURFACE.blit(obj, coordinates)


def draw_border() -> None:
    draw.rect(SURFACE, BLACK, BORDER)


# Define Background Class for bg
class Background(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = scale_image(load_image("Sprites", "space.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
