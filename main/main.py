from curses.ascii import ESC
import pygame
from pygame.locals import *

if __name__== "__main__": #main routine tha ky indiani po se di pse duhet
    pygame.init()
    surface = pygame.display.set_mode((540,720))
    surface.fill((255, 255, 255))

    floor = pygame.image.load("images/floor.png").convert()
    floor = pygame.transform.scale(floor,(128, 128))
    surface.blit(floor,(0,592))
    surface.blit(floor,(128,592))
    surface.blit(floor,(256,592))
    surface.blit(floor,(384,592))
    surface.blit(floor,(512,592))
    pygame.display.flip()


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == ESC:
                pass
            elif event.type == QUIT:
                running = False
            