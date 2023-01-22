from pygame import sprite, Surface, font
from constants import SURFACE, SCREEN_WIDTH
from colors import WHITE
from .images_helpers import load_image, scale_image
from sprites import score
from random import randrange

shotsperSecond: int = 5
lastshotTime: int = 0

# Load and Scale Turret Display
turretDisplayImage = load_image("New_Items", "TurretDisplay.png")
turretDisplayScaled = scale_image(
    turretDisplayImage, (turretDisplayImage.get_width()*1.5, turretDisplayImage.get_height()*1.5))

# Load turret image and scale it
turret_animation = [
    load_image("New_Items", "Turret_Image1.png"), load_image(
        "New_Items", "Turret_Image2.png"), 
    load_image("New_Items", "Turret_Image3.png"), load_image(
    "New_Items", "Turret_Image4.png"), 
    load_image("New_Items", "Turret_Image5.png") ]

# Load laser images
laser_start = load_image("New_Items", "Laser_Start.png")
laser_trail = load_image("New_Items", "Laser_Trail.png")
laser_end = load_image("New_Items", "Laser_End.png")

# Scale images
laserStartScaled = scale_image(laser_start, (laser_start.get_width()*4,laser_start.get_height()*4))
laserTrailScaled = scale_image(laser_trail, (laser_trail.get_width()*4,laser_trail.get_height()*4))
laserEndScaled = scale_image(laser_end, (laser_end.get_width()*4,laser_end.get_height()*4))

# Define Turret class
class Turret(sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.pos = pos
        self.shots = 10
        self.animation = turret_animation
        self.image = self.animation[0]
        self.rect = self.image.get_rect()
        self.gridnumber = round((pos[0]-120)/160)
        if self.gridnumber > 6:
            self.gridnumber = 6
        
        self.gridx = self.gridnumber*160 + 120
        self.rect.center = (self.gridx, pos[1] - 55)
        self.shootgroup = sprite.Group()
        self.nextframe = 0
        self.lastshotTime = score.scoretimer - 2500

    def draw(self, surface: Surface) -> None:
        sprites = self.shootgroup.sprites()
        for spr in sprites:
            spr.draw(surface)
        surface.blit(self.image, self.rect)

    def shoot(self, bombgroup, boxgroup) -> None:
        global shotsperSecond
        if score.scoretimer - self.lastshotTime > shotsperSecond*1000 and self.shots > 0:
            shotsperSecond = randrange(3,7)
            laser = Turret_Laser((self.gridx, self.pos[1] - 55))
            self.shootgroup.add(laser)
            self.lastshotTime = score.scoretimer
            self.shots -=1
        self.shootgroup.update(bombgroup, boxgroup)

    def update(self, bombgroup, boxgroup) -> None:
        self.nextframe += 1
        self.shoot(bombgroup, boxgroup)
        if self.nextframe // 4 >= 5:
            self.nextframe = 0
        self.image = self.animation[self.nextframe // 4]
        if self.shots == 0:
            self.kill()
        self.collision(bombgroup)

    def collision(self, bombgroup) -> None:
        if sprite.spritecollide(self, bombgroup, True):
            self.kill()


class TurretGroup(sprite.Group):
    def __init__(self) -> None:
        super().__init__()
    def draw(self,surface) -> None:
        sprites = self.sprites()
        for spr in sprites:
            spr.draw(surface)
turretGroup = TurretGroup()

def spawnTurret(pos) -> None:
    gridnumber = round((pos[0]-120)/160)
    sprites = turretGroup.sprites()
    occupied = False
    for spr in sprites:
        if spr.gridnumber == gridnumber:
            occupied = True
    if not occupied:
        new_turret = Turret(pos)
        turretGroup.add(new_turret)


class Turret_Laser(sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = laserStartScaled
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1] - 200)
        self.velocity = 4
        self.trailgroup = sprite.Group()
        self.end = Laser_End((pos[0],pos[1] - 112))
    
    
    def draw(self, surface: Surface) -> None:
        surface.blit(self.image, self.rect)
        sprites = self.trailgroup.sprites()
        for spr in sprites:
            spr.draw(surface)
        self.end.draw()

    def update(self, bombgroup, boxgroup) -> None:
        newlaser = Laser_Trail(self.rect.center)
        self.trailgroup.add(newlaser)
        self.rect.y -= self.velocity
        #draw.rect(SURFACE, (255, 0, 0), self.rect, 2)
        self.collision(bombgroup, boxgroup)

        if self.rect.y < -200 :
            self.trailgroup.remove(self.trailgroup)
            self.end.kill()
            self.kill()
    
    def collision(self, bombgroup, boxgroup) -> None:
        sprite.spritecollide(self, bombgroup, True)
        sprite.spritecollide(self, boxgroup, True)


class Laser_Trail(sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = laserTrailScaled
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1]+56)

    def draw(self, surface: Surface) -> None:
        surface.blit(self.image, self.rect)

class Laser_End(sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = laserEndScaled
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])
    
    def draw(self) -> None:
        SURFACE.blit(self.image, self.rect)

class TurretDisplay(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = turretDisplayScaled
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH - 200, 34)
        self.font = font.Font('upheavtt.ttf', 29)
        self.amount = 0
        self.text = self.font.render(str(self.amount), True, WHITE)
        self.textrect = self.text.get_rect()
        self.textrect.center = (self.rect.centerx - 40, self.rect.centery)

    def draw(self, surface: Surface) -> None:
        if self.amount > 0:
            surface.blit(self.image, self.rect)
            surface.blit(self.text, self.textrect)
            self.text = self.font.render(str(self.amount), True, WHITE)
    def update(self, amount) -> None:
        self.amount = amount

turretdisplaygroup = TurretGroup()
turretdisplay = TurretDisplay()
turretdisplaygroup.add(turretdisplay)