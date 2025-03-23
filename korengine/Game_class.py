from typing import List
from Log import *
from Entity_class import Entity
from Player import Player
import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen
        Log.log('game is initiated')
        self.allEntities: List[Entity] = []


        


    def AddEntity(self, ent):
        self.allEntities.append(ent)

    def Update(self, Deltatime):
        
        for e in self.allEntities:
            e.Update(Deltatime)

    
    def Render(self):
         for e in self.allEntities:
            e.Render(self.screen)

    def LoadAssets(self):
        
        smileyImage = pygame.image.load("korengine\\Assets\\smiley.png")
        self.AddEntity(Player("player", (0,0), smileyImage))
        pass
    def Onquit(self):
        Log.log('ONQUIT')
        pass