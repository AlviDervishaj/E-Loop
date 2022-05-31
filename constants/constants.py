from pygame import Surface, display, font, mixer, Rect

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
VELOCITY: int = 10

# frames per second, may need later
FPS: int = 60

# max number of bombs in screen, number of frames needed to spawn a rocket
BOMB_MAX: int = 5
BOMB_TIME: int = 10
