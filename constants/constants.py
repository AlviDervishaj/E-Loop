from pygame import Surface, display, font, mixer, Rect, USEREVENT

# initialize font
font.init()
# initialize sound
mixer.init()
# width and height of the window
SCREEN_WIDTH: int = 1280
SCREEN_HEIGHT: int = 720

# display instance
DISPLAY: display = display

# window instance
SURFACE: Surface = DISPLAY.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define border so that we know what is off-screen and on screen
BORDER: Rect = Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

# Moving Velocity
VELOCITY: int = 8

# frames per second, may need later
FPS: int = 120

# max number of bombs in screen, number of frames needed to spawn a rocket
BOMB_MAX: int = 30
BOMB_TIME: int = 4
BOMB_WAVE_MIN: int = 5

# for Questions
QUESTION_TIME = 60
# Question event
NEW_QUESTION = USEREVENT
# Game Over Event
DEATH = USEREVENT + 1
# Damage
PLAYER_DAMAGE = USEREVENT + 2