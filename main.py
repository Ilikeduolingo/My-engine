import pygame
import time
from Game_class import *
from Log import *
import Global_options
import sys
pygame.init()
Log.initialise()
Log.log('Pygame initialised skibidi')
screen = pygame.display.set_mode((Global_options.SCREENW, Global_options.SCREENH))
clock = pygame.time.Clock() #frames per tick
running = True
game = Game(screen)
Log.log('created game instance ')
game.LoadAssets()
while running:
    start_time = time.time()
    dt = clock.tick(Global_options.FPS)/1000
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    game.Update(dt)
    game.Render()
    end_time = time.time()
    diff = end_time-start_time
    Log.log(f'skbidi toilet loves {dt}')
    #print(1/diff)
    pygame.display.flip()
game.Onquit()
