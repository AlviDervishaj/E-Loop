from random import randrange
import pygame as p
from pygame import Surface
from constants import SCREEN_WIDTH
from .images_helpers import load_image, scale_image

# load bomb image and scale it
bomb_surface: Surface = load_image("Sprites", "Bomb_TRANS.png")
BOMB: Surface = scale_image(
    bomb_surface, (bomb_surface.get_width()*3, bomb_surface.get_height()*3))

# Define collision detection, later will detect collision with barriers as well
def collision_detect(bomb, floor, character) -> None:
    if p.sprite.groupcollide(bomb, floor, True, False):
        print("Life lost")
    elif p.sprite.groupcollide(bomb, character, True, False):
        print("You dead boi")


# Define Bomb class
class Bomb(p.sprite.Sprite):
    def __init__(self, bomb: Surface) -> None:
        super().__init__()
        self.image = bomb
        self.rect = self.image.get_rect()
        self.rect.center = (randrange(0, SCREEN_WIDTH), -200)

    def update(self) -> None:
        self.rect.y += 10


# Create Bomb group
bomb = Bomb(BOMB)
bomb_group = p.sprite.Group()
bomb_group.add(bomb)

# Create function to generate bomb


def bomb_spawn() -> Bomb:
    return Bomb(BOMB)
