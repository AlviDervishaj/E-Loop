from pygame import sprite
from helpers import Background, Character, char_walk_scaled, char_still_scaled, FLOOR, Floor

background = Background()
character = Character(char_walk_scaled, char_still_scaled)
floor = Floor(FLOOR)



background_group = sprite.Group()
character_group = sprite.Group()
floor_group = sprite.Group()

# add to background group
background_group.add(background)
character_group.add(character)
floor_group.add(floor)
