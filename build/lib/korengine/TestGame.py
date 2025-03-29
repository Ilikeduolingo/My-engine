from typing import List
from Log import *
from Entity_class import Entity
from Player import Player
import pygame
from Game_class import Game
from client import *
from server import *
import threading

class TestGame(Game):
    def __init__(self, screen):
        super().__init__(screen)

        self.server_thread = threading.Thread(target=self.RunServer, daemon=True)       
        self.server_thread.start()      

    def RunClient(self):
        asyncio.run(start_client())

    def RunServer(self):
        asyncio.run(start_server())


    def Update(self, Deltatime):

        super().Update(Deltatime)



