#This class represents and entity in the game engine
from Log import *
class Entity: 
    def __init__(self, name):
        self.name = name
        pass

    def Update(self, DeltaTime):
        Log.log(f"Updating entity {self.name}")
        pass

    def Render(self):
        Log.log(f"Rendering entity {self.name}")

        pass