import pygame 

pygame.init()

#player class to define player position
class Player():
    def __init__ (self, x, y ):
        self.x = x
        self.y = y 
    
    def pos_change(self,changex):
        self.changex = changex
        return changex

    def pos_changeY(self,changeY):
        self.changeY = changeY
        return changeY
    


