from pygame import Surface, display, font, mixer, Rect

# initialize font
font.init()
# initialize sound
mixer.init()
# width and height of the window
SCREEN_WIDTH: int = 540
SCREEN_HEIGHT: int = 720

# display instance
DISPLAY: display = display

# window instance
SURFACE: Surface = DISPLAY.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define border so that we know what is off-screen and on screen
BORDER: Rect = Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

# Moving Velocity
VELOCITY: int = 5

# frames per second, may need later
FPS: int = 60
