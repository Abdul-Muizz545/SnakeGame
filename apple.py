from random import randint
import pygame

class Apple:
    """Class for creating an apple"""
    COLOR = (255, 0, 0) #ALL apples should be red

    #constructor
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    #function to draw apple onto window
    def drawApple(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height), 0)


    #function to make new apple when snake eats apple
    def generateNewApple(self, snake, win):
        numberOfCols = win.get_width() // 10
        numberOfRows = win.get_height() // 10 
        #print(numberOfRows, numberOfCols)

        scaled_apple_x = randint(0, numberOfCols - 1) #generate random integer
        scaled_apple_y = randint(0, numberOfRows - 1) #generate random integer

        new_apple_x = scaled_apple_x * 10
        new_apple_y = scaled_apple_y * 10
        return Apple(new_apple_x, new_apple_y, self.width, self.height)
         







        