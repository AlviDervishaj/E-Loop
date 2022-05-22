from random import randrange
import pygame as p
from pygame import Surface
from constants import SCREEN_WIDTH, BOMB_MAX, BOMB_TIME
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
        self.rect.center = (randrange(50, SCREEN_WIDTH-50, 50), -200)

    def update(self) -> None:
        self.rect.y += 10
        



# Create function to generate bomb
def bomb_spawn() -> Bomb:
    return Bomb(BOMB)
# Create function to generate bomb after set amount of seconds
def handle_bomb_spawn(group, bomb_timer) -> None:

    if len(group) < BOMB_MAX and bomb_timer >= BOMB_TIME:
            bomb_timer = 0
            new_bomb = bomb_spawn()
            group.add(new_bomb)