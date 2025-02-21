from Log import *
class Game:
    def __init__(self, screen):
        self.screen = screen
        Log.log('game is initiated')
    def Update(self, Deltatime):
        Log.log('UPDATE')
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