from .images_helpers import scale_image, load_image
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame import sprite, mouse

# Import all sprites for pointer
pointer_surface = load_image("Sprites", "Pointer.png")

# Scale all sprites for shield
POINTER = scale_image(
    pointer_surface, (pointer_surface.get_width()*1.5, pointer_surface.get_height()*1.5))


# Define Pointer class
class Pointer(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = POINTER
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT
    def update(self) -> None:
        self.rect.x = mouse.get_pos()[0]
        self.rect.y = mouse.get_pos()[1]