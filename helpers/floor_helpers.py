from .images_helpers import scale_image, load_image
from pygame import Surface, Rect
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

floor_surface: Surface = load_image("floor.png")

FLOOR: Surface = scale_image(floor_surface, (SCREEN_WIDTH, floor_surface.get_height() * 10))

(FLOOR_WIDTH, FLOOR_HEIGHT) = FLOOR.get_size()

FLOOR_POSITION = (0, SCREEN_HEIGHT - FLOOR.get_height())

# Hit Box
# used to check collisions
floor_hit_box: Rect = Rect(0, SCREEN_HEIGHT - 28, FLOOR_WIDTH, 28)
