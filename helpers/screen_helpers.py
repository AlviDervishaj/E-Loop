from pygame import Surface, draw
from constants import SURFACE, BORDER
from colors import BLACK


def fill_surface_with_color(color: tuple) -> None:
    SURFACE.fill(color)


def blit_surface(obj: Surface, coordinates: tuple) -> None:
    SURFACE.blit(obj, coordinates)


def draw_border() -> None:
    draw.rect(SURFACE, BLACK, BORDER)
