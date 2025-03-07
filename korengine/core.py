from Game_class import *
import pygame
import time
from Log import *
from Global_options import *
class Core:
    game_instace = None
    @staticmethod
    def Start(game:Game):
        Log.log('Pygame initialised skibidi')

        game_instsance = game
        game_instsance.LoadAssets()
        clock = pygame.time.Clock() #frames per tick
        running = True
        Log.log('created game instance ')
        game.LoadAssets()
        while running:
            start_time = time.time()
            dt = clock.tick(60)/1000
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


           