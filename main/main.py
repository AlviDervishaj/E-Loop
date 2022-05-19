from curses.ascii import ESC
import pygame
from pygame.locals import *

if __name__== "__main__": #main routine tha ky indiani po se di pse duhet
    pygame.init()
    surface = pygame.display.set_mode((540,720))
    surface.fill((255, 255, 255))

#floor
    floor = pygame.image.load("images/floor.png").convert()
    floor = pygame.transform.scale(floor,(256, 256))
    surface.blit(floor,(0,464))
    surface.blit(floor,(256,464))
    surface.blit(floor,(512,464))
    
#character
    character = pygame.image.load("images/character.png").convert()
    character = pygame.transform.scale(character,(256, 256))
    surface.blit(character,(135,464))


    pygame.display.flip()
#main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == ESC:
                pass
            elif event.type == QUIT:
                running = False
            