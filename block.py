import pygame

class Block:
    """Class for creating a Block"""

    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.xspeed = 10
        self.yspeed = 0
        self.color = colour #color of each block

    #Method to draw block
    def drawBlock(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(win, (0,0,255), (self.x, self.y,self.width,self.height), 1)

    #method to update speed of block according to key presses (receives event parameter)
    def updateSpeed(self, keys, win):
        if not (self.xspeed > 0) and keys[pygame.K_LEFT]: #if not moving to right and pressed left
            self.xspeed = -10
            self.yspeed = 0

        elif not (self.xspeed < 0) and keys[pygame.K_RIGHT]: #if not moving to left and pressed right            
            self.xspeed = 10
            self.yspeed = 0
        
        elif not (self.yspeed < 0) and keys[pygame.K_DOWN]: #if not moving up and pressing down
            self.yspeed = 10
            self.xspeed = 0

        elif not (self.yspeed > 0) and keys[pygame.K_UP]: #if not moving down and pressing up
            self.yspeed = -10
            self.xspeed = 0

    