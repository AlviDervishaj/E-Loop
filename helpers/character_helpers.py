from pygame import Surface, Rect
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from .images_helpers import scale_image, load_image
from .floor_helpers import FLOOR_HEIGHT

# load image
character_surface: Surface = load_image("character.png")

CHARACTER: Surface = scale_image(character_surface, (128, 128))
(CHARACTER_WIDTH, CHARACTER_HEIGHT) = CHARACTER.get_size()

CHARACTER_X = SCREEN_WIDTH / 2 - CHARACTER.get_width() / 2
CHARACTER_Y = SCREEN_HEIGHT - FLOOR_HEIGHT + 100
# Hit Box
# Use to check collisions
character_hit_box: Rect = Rect(CHARACTER_X, CHARACTER_Y, CHARACTER_WIDTH, CHARACTER_HEIGHT)

