from pygame import sprite
from helpers import Background, Character, Bomb, char_walk_scaled, char_still_scaled, FLOOR, BOMB, Floor

# add instances for each class
background = Background()
character = Character(char_walk_scaled, char_still_scaled)
floor = Floor(FLOOR)
bomb = Bomb(BOMB)



# add groups for all sprites
background_group = sprite.Group()
character_group = sprite.Group()
floor_group = sprite.Group()
bomb_group = sprite.Group()

# add classes to each group
background_group.add(background)
character_group.add(character)
floor_group.add(floor)
bomb_group.add(bomb)
