from pygame import sprite, event, draw
from sprites import score
from constants import SCREEN_WIDTH, ADDTURRET, SURFACE
from random import randrange
from .images_helpers import load_image, scale_image

drop_images = [load_image("New_Items", "Risk_Drop.png"), load_image(
    "New_Items", "Shield_Drop.png"), load_image("New_Items", "Heart_Drop.png")]
drop_scaled = [scale_image(drop_images[0], (drop_images[0].get_width()*3, drop_images[0].get_height()*3)),
            scale_image(
                drop_images[1], (drop_images[1].get_width()*3, drop_images[1].get_height()*3)),
            scale_image(
                drop_images[2], (drop_images[2].get_width()*3, drop_images[2].get_height()*3))]

dropGroup = sprite.Group()
lastSpawnTime = 0
dropTime = 30

def dropSpawn() -> None:
    global lastSpawnTime, dropTime, dropGroup
    if score.scoretimer - lastSpawnTime > dropTime*1000:
        lastSpawnTime = score.scoretimer
        dropTime = randrange(30,46)
        type = randrange(0,3)
        newdrop = Drop_Item(type)
        dropGroup.add(newdrop)

class Drop_Item(sprite.Sprite):
    def __init__(self, type) -> None:
        super().__init__()
        self.type = type
        self.images = drop_scaled
        self.image = self.images[self.type]
        self.rect = self.image.get_rect()
        self.rect.center = (randrange(40, SCREEN_WIDTH-39, 80), -200)
        self.velocity = 3

    def update(self, floor: sprite.Group, character: sprite.Group) -> None:
        self.rect.y += self.velocity
        self.collision(floor, character)
        # Hitbox Purposes only
        draw.rect(SURFACE, (255, 0, 0), self.rect, 2)

    def collision(self, floor: sprite.Group, character: sprite.Group) -> None:
        global dropGroup
        if sprite.spritecollide(self, floor, False):
            self.velocity = 0
        if sprite.spritecollide(self, character, False):
            event.post(event.Event(ADDTURRET + self.type))
            self.kill()
