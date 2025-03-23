import pygame

#This class represents and entity in the game engine
from Log import *
class Entity: 
    def __init__(self, name, position:pygame.Vector2 = (0,0), image: pygame.Surface = None):
        self.name = name
        self.position = position
        self.image = image
        pass

    def Update(self, DeltaTime):

        pass

    def Render(self, screen: pygame.Surface):
        if self.image != None:
            screen.blit(self.image, self.position)

        pass