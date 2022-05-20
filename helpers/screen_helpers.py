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


def draw_background_sky(image_path: str) -> None:
    image: Surface = load_image(image_path)
    # resize
    resized_image: Surface = scale_image(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    SURFACE.blit(resized_image, (0, 0))
