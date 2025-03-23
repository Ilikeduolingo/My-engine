from typing import List
from Log import *
from Entity_class import Entity

class Game:
    def __init__(self, screen):
        self.screen = screen
        Log.log('game is initiated')
        self.allEntities: List[Entity] = []

        test = Entity("Matt mcnilly")
        self.AddEntity(test)

        self.AddEntity(Entity("player"))


    def AddEntity(self, ent):
        self.allEntities.append(ent)

    def Update(self, Deltatime):
        
        for e in self.allEntities:
            e.Update(Deltatime)

    
    def Render(self):
         for e in self.allEntities:
            e.Render()

    def LoadAssets(self):
        Log.log('LOADASSETS')
        pass
    def Onquit(self):
        Log.log('ONQUIT')
        pass