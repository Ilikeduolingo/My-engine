class Game:
    def __init__(self, screen):
        self.screen = screen
        print('game is initiated')
    def Update(self, Deltatime):
        print('UPDATE')
        pass
    def Render(self):
        print('RENDER')
        pass
    def LoadAssets(self):
        print('LOADASSETS')
        pass
    def Onquit(self):
        print('ONQUIT')
        pass