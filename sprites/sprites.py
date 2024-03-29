from pygame import sprite
from helpers import Background, char_walk_right_scaled, char_walk_left_scaled, char_still_scaled
from helpers import Floor, Character, Bomb, Pointer, Question_Drop, Score, HUD_Display
# add instances for each class
background = Background()
character = Character(char_walk_right_scaled, char_walk_left_scaled, char_still_scaled)
floor = Floor()
pointer = Pointer()
question_drop = Question_Drop()
score = Score()
HUD_object = HUD_Display()
# add groups for all sprites
background_group = sprite.Group()
character_group = sprite.Group()
floor_group = sprite.Group()
bomb_group = sprite.Group()
shield_group = sprite.Group()
pointer_group = sprite.Group()
question_drop_group = sprite.Group()
popup_group = sprite.Group()

# add classes to each group
background_group.add(background)
character_group.add(character)
floor_group.add(floor)
pointer_group.add(pointer)
