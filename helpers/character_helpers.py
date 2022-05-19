from pygame import Surface, image, Rect
from os import path
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

# get image path
CHARACTER_PATH: str = path.join("images", "character.png")

# load image
CHARACTER: Surface = image.load(CHARACTER_PATH)
(CHARACTER_WIDTH, CHARACTER_HEIGHT) = CHARACTER.get_size()
# Hit Box
# Use to check collisions
character_hit_box: Rect = Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3, CHARACTER_WIDTH, CHARACTER_HEIGHT)

