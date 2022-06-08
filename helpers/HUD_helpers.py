from colors import WHITE
from pygame import Surface, sprite, time, font
from constants import SCREEN_WIDTH, SURFACE
from .images_helpers import load_image, scale_image


# Class for all HUD objects
class HUD_Display(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.shield = Shield_Durability()
        self.shield.draw()
        self.shield_amount = Amount_Display()
        self.shield_amount.draw()
        self.heart = [ 
            Display_Heath(0), 
            Display_Heath(1), 
            Display_Heath(2), 
            Display_Heath(3), 
            Display_Heath(4)
            ]
    def draw(self) -> None:
        # Draw all hud elements
        self.shield.draw()
        self.shield_amount.draw()

    def update(self, durability, shield_group, shield_amount) -> None:
        # update shield_durability
        self.shield.update(durability, shield_group)
        # update shield_amount
        self.shield_amount.update(shield_amount)
    def draw_health(self, health) -> None:
        for i in range(health):
            self.heart[i].draw()

# Load and scale all images for Displaying Shield amount
shield1 = load_image("Shield_Display", "SHdisplay1.png")
display_shield = [
    load_image("Shield_Display", "SHdisplay1.png"), load_image(
        "Shield_Display", "SHdisplay2.png"),
    load_image("Shield_Display", "SHdisplay3.png"), load_image(
        "Shield_Display", "SHdisplay4.png"),
    load_image("Shield_Display", "SHdisplay5.png"), load_image(
        "Shield_Display", "SHdisplay6.png"),
    load_image("Shield_Display", "SHdisplay7.png"), load_image(
        "Shield_Display", "SHdisplay8.png"),
    load_image("Shield_Display", "SHdisplay9.png"), load_image(
        "Shield_Display", "SHdisplay10.png")
]

SCALED_SHIELD = [
    scale_image(display_shield[0], (shield1.get_width()*4, shield1.get_height()*4)), scale_image(
        display_shield[1], (shield1.get_width()*4, shield1.get_height()*4)),
    scale_image(display_shield[2], (shield1.get_width()*4, shield1.get_height()*4)), scale_image(
        display_shield[3], (shield1.get_width()*4, shield1.get_height()*4)),
    scale_image(display_shield[4], (shield1.get_width()*4, shield1.get_height()*4)), scale_image(
        display_shield[5], (shield1.get_width()*4, shield1.get_height()*4)),
    scale_image(display_shield[6], (shield1.get_width()*4, shield1.get_height()*4)), scale_image(
        display_shield[7], (shield1.get_width()*4, shield1.get_height()*4)),
    scale_image(display_shield[8], (shield1.get_width()*4, shield1.get_height()*4)), scale_image(
        display_shield[9], (shield1.get_width()*4, shield1.get_height()*4))
]


# Create Durability Class
class Shield_Durability(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.states = SCALED_SHIELD
        self.image = self.states[9]
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH - 70, 35)

    def draw(self) -> None:
        SURFACE.blit(self.image, self.rect)

    def update(self, durability, group) -> None:
        self.image = self.states[9 - durability]
        if len(group) < 1:
            self.image = self.states[9]


# Create Display_Amount Class
class Amount_Display(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.amount = 0
        self.font = font.Font('upheavtt.ttf', 29)
        self.text = self.font.render(str(self.amount), True, WHITE)
        self.textrect = self.text.get_rect()
        self.textrect.center = (SCREEN_WIDTH - 145, 34)

    def draw(self) -> None:
        self.text = self.font.render(str(self.amount), True, WHITE)
        SURFACE.blit(self.text, self.textrect)

    def update(self, amount) -> None:
        self.amount = amount


# Load and scale heart image
heart_surface: Surface = load_image("Shield_Display", "Heart.png")
HEART: Surface = scale_image(
    heart_surface, (heart_surface.get_width()*2, heart_surface.get_height()*2))


# Create Display_Health Class
class Display_Heath(sprite.Sprite):
    def __init__(self, index: int) -> None:
        super().__init__()
        self.image = HEART
        self.rect = self.image.get_rect()
        self.rect.center = (35 + index*30,25)
    def draw(self) -> None:
        SURFACE.blit(self.image, self.rect)
