from random import randrange
from pygame import Surface, sprite, time, draw
from constants import SCREEN_WIDTH, BOMB_MAX, BOMB_TIME, SURFACE
from .images_helpers import load_image, scale_image

# load bomb image and scale it
bomb_surface: Surface = load_image("Sprites", "Bomb_TRANS.png")
BOMB: Surface = scale_image(
    bomb_surface, (bomb_surface.get_width()*3, bomb_surface.get_height()*3))

# Spawn_time variable
Spawn_time = 0


# Define collision detection, later will detect collision with barriers as well
def collision_detect(bomb, floor, character) -> None:
    if sprite.groupcollide(bomb, floor, True, False):
        print("0")
    elif sprite.groupcollide(bomb, character, True, False):
        print("You dead boi")


# Define Bomb class
class Bomb(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = BOMB
        self.rect = self.image.get_rect()
        self.rect.center = (randrange(50, SCREEN_WIDTH-50, 50), -200)

    def update(self) -> None:
        self.rect.y += 10
        # Hitbox Purposes only
        draw.rect(SURFACE, (255, 0, 0), self.rect, 2)


# Function for handling difficulty
def difficulty_handler(timeP) -> int:
    x = time.get_ticks() - timeP
    x = x//(BOMB_TIME*1000)
    if x >= BOMB_TIME - 0.15:
        x = BOMB_TIME - 0.1
    return x


# Create function to generate bomb
def bomb_spawn() -> Bomb:
    return Bomb()


# Create function to generate bomb after set amount of seconds
def handle_bomb_spawn(group, timeP) -> None:
    global Spawn_time
    bomb_timer = time.get_ticks()
    bomb_timer -= Spawn_time
    if len(group) < BOMB_MAX and bomb_timer/1000 > BOMB_TIME - difficulty_handler(timeP):

        Spawn_time = time.get_ticks()
        new_bomb = bomb_spawn()
        group.add(new_bomb)
