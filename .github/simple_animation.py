# Simple Animation with Pygame, Jaden Terry, 01/05/21, 2:35pm, v0.1

import pygame, sys, time
from pygame.locals import *

# setup Pygame
pygame.init()

# Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mod((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')
