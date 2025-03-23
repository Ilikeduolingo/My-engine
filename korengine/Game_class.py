from typing import List
from Log import *
from Entity_class import Entity

class Game:
    def __init__(self, screen):
        self.screen = screen
        Log.log('game is initiated')
        self.allEntities: List[Entity] = []

        test = Entity('Matt Mcnally')
        self.AddEntity(test)


    def AddEntity(self, ent):
        self.allEntities.append(ent)
    def Update(self, Deltatime):
        Log.log('UPDATE')
        
        for e in self.allEntities:
            e.Update(Deltatime)

        pass
    def Render(self):
        Log.log('RENDER')
        pass
    def LoadAssets(self):
        Log.log('LOADASSETS')
        pass
    def Onquit(self):
        Log.log('ONQUIT')
        pass