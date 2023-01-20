from random import randrange
from pygame import Surface, sprite, time, event, font
from constants import SCREEN_WIDTH, BOMB_MAX, BOMB_TIME, SURFACE, PLAYER_DAMAGE, BOMB_WAVE_MIN
from colors import RED
from math import floor
from .images_helpers import load_image, scale_image

# load bomb image and scale it
bomb_surface: Surface = load_image("Sprites", "Bomb_TRANS.png")
BOMB: Surface = scale_image(
    bomb_surface, (bomb_surface.get_width()*3, bomb_surface.get_height()*3))

# Spawn_time variable
Spawn_time = 0
Bomb_count = 1
Wave_index: int = 0
Wavemin: float = 0
Wavemax: float = 5

# Define collision detection, later will detect collision with barriers as well


def collision_detect(bomb, floor, character) -> None:
    if sprite.groupcollide(bomb, floor, True, False):
        pass
    elif sprite.groupcollide(bomb, character, True, False):
        event.post(event.Event(PLAYER_DAMAGE))


# Define Bomb class
class Bomb(sprite.Sprite):
    def __init__(self, i) -> None:
        super().__init__()
        self.image = BOMB
        self.rect = self.image.get_rect()
        self.rect.center = (randrange(10, SCREEN_WIDTH-10, 30), -(500*i))
        self.velocity = randrange(3,20)
    def update(self) -> None:
        self.rect.y += self.velocity
        # Hitbox Purposes only
        #draw.rect(SURFACE, (255, 0, 0), self.rect, 2)


# Function for handling difficulty
def difficulty_handler(wave_index) -> int:
    minus_time = wave_index*0.5
    if minus_time >= BOMB_TIME - 0.65:
        minus_time = BOMB_TIME - 0.6
    return minus_time


# Create function to generate bomb
def bomb_spawn(i) -> Bomb:
    return Bomb(i)


# Create function to spawn based on waves
def handle_bomb_spawn(group: sprite.Group) -> None:
    global Bomb_count, Wavemin, Wavemax
    amount_spawned = randrange(0, floor(Wavemax))
    print(amount_spawned)
    Bomb_count += amount_spawned
    for i in range(floor(Wavemin) + amount_spawned):
        new_bomb = bomb_spawn(i)
        group.add(new_bomb)


# Create function to generate bomb after set amount of seconds
def handle_bomb_wave(group: sprite.Group, timepaused) -> None:
    global Spawn_time, Bomb_count, Wave_index
    global Wavemin, Wavemax
    bomb_timer = time.get_ticks() - timepaused
    bomb_timer -= Spawn_time
    if Bomb_count > (BOMB_WAVE_MIN + Wave_index*10):
        Wave_index += 1
        Wavemin += 0.3
        Wavemax += 0.7
        print(Wavemax)
    if len(group) < BOMB_MAX and bomb_timer/1000 > BOMB_TIME - difficulty_handler(Wave_index):
        Spawn_time = time.get_ticks()
        handle_bomb_spawn(group)


# Create score class
class Score(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.font = font.Font('upheavtt.ttf', 40)
        self.score = 0
        self.text = self.font.render(str(int(self.score)), True, RED)
        self.textrect = self.text.get_rect()
        self.textrect.center = (SCREEN_WIDTH/2, 20)

    def draw(self) -> None:
        SURFACE.blit(self.text, self.textrect)

    def update(self, time_paused) -> None:
        scoretimer = time.get_ticks() - time_paused
        self.score = scoretimer / 500 
        self.text = self.font.render(str(int(self.score)), True, RED)

    def myscore(self) -> int:
        return int(self.score)
