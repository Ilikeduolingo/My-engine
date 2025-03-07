import pygame
import time
from Game_class import *
from Log import *
import Global_options
import sys
from core import *
pygame.init()
screen = pygame.display.set_mode((Global_options.SCREENW, Global_options.SCREENH))
running = True
game = Game(screen)
Core.Start(game)
