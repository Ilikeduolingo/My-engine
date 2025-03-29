from Entity_class import *
from Log import *
class Player(Entity):
     def __init__(self, name, position:pygame.Vector2 = (0,0), image: pygame.Surface = None):
        super().__init__( name, position, image) 
        pass
     
     def Update(self, DeltaTime):


        pass