from typing import List
from korengine.Log import *
from korengine.Entity_class import Entity
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
         self.screen.fill((0,0,0))
         for e in self.allEntities:
            e.Render(self.screen)

    def LoadAssets(self):
        Log.log('Loading da assets')
    def Onquit(self):
        Log.log('ONQUIT')
        pass