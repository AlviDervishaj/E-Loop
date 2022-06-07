from random import randrange
from pygame import Surface, sprite, time, event, font
from constants import SCREEN_WIDTH, BOMB_MAX, BOMB_TIME, SURFACE, DEATH
from colors import RED
from constants.constants import SCREEN_HEIGHT
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
        pass
    elif sprite.groupcollide(bomb, character, True, False):
        event.post(event.Event(DEATH))


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
        #draw.rect(SURFACE, (255, 0, 0), self.rect, 2)

# Function for handling difficulty
def difficulty_handler(time_paused) -> int:
    _handle_time = time.get_ticks() - time_paused
    x = _handle_time // (BOMB_TIME * 1000)
    if x >= BOMB_TIME - 0.25:
        x = BOMB_TIME - 0.2
    return x


# Create function to generate bomb
def bomb_spawn() -> Bomb:
    return Bomb()


# Create function to generate bomb after set amount of seconds
def handle_bomb_spawn(group, time_paused) -> None:
    global Spawn_time
    bomb_timer = time.get_ticks()
    bomb_timer -= Spawn_time
    if len(group) < BOMB_MAX and bomb_timer/1000 > BOMB_TIME - difficulty_handler(time_paused):

        Spawn_time = time.get_ticks()
        new_bomb = bomb_spawn()
        group.add(new_bomb)

# Create score class

class Score(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.font = font.Font('upheavtt.ttf', 40)
        self.score = 0
        self.text = self.font.render(str(int(self.score)), True, RED)
        self.textrect = self.text.get_rect()
        self.textrect.center = (SCREEN_WIDTH/2, 30)

    def draw(self) -> None:
        SURFACE.blit(self.text, self.textrect)
    def update(self, time_paused) -> None:
        scoretimer = time.get_ticks() - time_paused
        self.score = scoretimer / 500
        self.text = self.font.render(str(int(self.score)), True, RED)
    
    def myscore(self) -> int:
        return int(self.score)