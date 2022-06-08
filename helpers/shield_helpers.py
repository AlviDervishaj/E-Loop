from .images_helpers import scale_image, load_image
from pygame import sprite

# Import all sprites for shield/shield animation - for later
shield_surface = load_image("Sprites", "Shield_PROT1.png")

# Scale all sprites for shield
SHIELD = scale_image(
    shield_surface, (shield_surface.get_width()*5, shield_surface.get_height()*5))


# Define shield class
class Shield(sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = SHIELD
        self.rect = self.image.get_rect()
        self.durability = 9
        self.rect.center = pos

    # Damage function for the shield
    def damage(self) -> None:
        self.durability -= 1
        if self.durability <= 0:
            self.kill()

    # Updates shield position and detects shield collision
    def update(self, pos, bomb) -> None:
        self.rect.centerx = pos[0]
        self.collision(bomb)

    # When collision is detected the damage function is called
    def collision(self, bomb) -> None:
        if sprite.spritecollide(self, bomb, True):
            self.damage()
    def get_durability(self) -> int:
        return self.durability
