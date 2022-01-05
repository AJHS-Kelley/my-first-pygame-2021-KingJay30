# Simple Animation with Pygame, Jaden Terry, 01/05/21, 2:44pm, v0.2

import pygame, sys, time
from pygame.locals import *

# setup Pygame
pygame.init()

# Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mod((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

# Setup the direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4