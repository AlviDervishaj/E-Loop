from curses.ascii import ESC
import pygame
from pygame.locals import *

if __name__== "__main__": #main routine tha ky indiani po se di pse duhet
    pygame.init()
    surface = pygame.display.set_mode((540,720))
    surface.fill((255, 225, 148))
    pygame.display.flip()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == ESC:
                pass
            elif event.type == QUIT:
                running = False
            