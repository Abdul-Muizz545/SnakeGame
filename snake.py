import pygame
from block import Block

class Snake:
    """Class for creating a snake"""
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

    #constructor for Snake
    def __init__(self, x, y, width, height):
        self.blocks = [] #array to store blocks of snake
        self.head = Block(x + 4 * width, y, width, height, self.BLUE) #head of snake 

        #start off with length of 5
        self.blocks.append(self.head)
        self.blocks.append(Block(x + 3 * width, y, width, height, self.GREEN)) 
        self.blocks.append(Block(x + 2 * width, y, width, height, self.GREEN)) 
        self.blocks.append(Block(x + 1 * width, y, width, height, self.GREEN)) 
        self.blocks.append(Block(x, y, width, height, self.GREEN))

    #method to move snake
    def moveSnake(self, keys, win):
        if self.blocks[0].xspeed != 0 or self.blocks[0].yspeed != 0:
            self.head.updateSpeed(keys, win)
            prevHead = self.blocks[0]        
            prevHead.color = self.GREEN
            self.blocks.insert(0, Block(prevHead.x + prevHead.xspeed, prevHead.y + prevHead.yspeed, prevHead.width, prevHead.height, self.BLUE))
            self.blocks[0].xspeed = prevHead.xspeed
            self.blocks[0].yspeed = prevHead.yspeed
            self.head = self.blocks[0]
            self.blocks.pop() #remove last block of snake
        
    #method called when snake eats apple (increase snake length)
    def growSnake(self):
        snake_tail = self.blocks[len(self.blocks) - 1] #gets tail of snale
        self.blocks.insert(len(self.blocks), Block(snake_tail.x + snake_tail.xspeed, snake_tail.y + snake_tail.yspeed, snake_tail.width, snake_tail.height, self.GREEN))
        #print(snake_tail.xspeed, snake_tail.yspeed)

    

    #Method to draw snake
    def drawSnake(self, win):
        for i in range(len(self.blocks)):
            self.blocks[i].drawBlock(win)

    #method to detect if snake ate apple or not
    def eatenApple(self, apple):
        if self.head.x == apple.x and self.head.y == apple.y:
            return True
        else:
            return False

    #method to detect when the head of snake collides with sth and return True or False
    def detectCollisionWithWalls(self, win):
        if (self.head.x <= 0) or (self.head.x >= win.get_width() - self.head.width):
            return True  
        if (self.head.y <= 0) or (self.head.y >= win.get_height() - self.head.height):
            return True
        return False   

    #method that returns true if you hit yourself, otherwise false
    def detectCollisionIntoSelf(self):
        for i in range(1, len(self.blocks)):
            if self.head.x == self.blocks[i].x and self.head.y == self.blocks[i].y:
                return True
        return False
    

    #method to handle snake collision with walls
    #if it returns true, it means player lost game
    #if it returns false, then that means that player didnt lose yet
    def handleCollisionWithWalls(self, keys, win):
        #CASE 1 - collide with upper left corner
        if (self.head.x <= 0) and (self.head.y <= 0):
            if self.head.xspeed != 0 and self.head.yspeed == 0:
                self.head.xspeed = 0

                if keys[pygame.K_DOWN]:
                    self.head.yspeed = 10
                else:
                    print("You lose!")
                    return True

            elif self.head.xspeed == 0 and self.head.yspeed != 0:
                self.head.yspeed = 0
                
                if keys[pygame.K_RIGHT]:
                    self.head.xspeed = 10
                else:
                    print("You lose")
                    return True

        #CASE 2 - collide with upper right corner
        elif (self.head.x >= win.get_width() - self.head.width) and (self.head.y <= 0):
            if self.head.xspeed != 0 and self.head.yspeed == 0:
                self.head.xspeed = 0

                if keys[pygame.K_DOWN]:
                    self.head.yspeed = 10
                else:
                    print("You lose!")
                    return True


            elif self.head.xspeed == 0 and self.head.yspeed != 0:
                self.head.yspeed = 0
                
                if keys[pygame.K_LEFT]:
                    self.head.xspeed = -10
                else:
                    print("You lose")
                    return True

        #CASE 3 - Collide with Bottom left corner
        elif (self.head.x <= 0) and (self.head.y >= win.get_height() - self.head.height):
            if self.head.xspeed != 0 and self.head.yspeed == 0:
                self.head.xspeed = 0

                if keys[pygame.K_UP]:
                    self.head.yspeed = -10
                else:
                    print("You lose!")
                    return True

            elif self.head.xspeed == 0 and self.head.yspeed != 0:
                self.head.yspeed = 0
                
                if keys[pygame.K_RIGHT]:
                    self.head.xspeed = 10
                else:
                    print("You lose")
                    return True

        #CASE 4 - Collide with bottom right corner
        elif (self.head.x >= win.get_width() - self.head.width) and (self.head.y >= win.get_height() - self.head.height):
            if self.head.xspeed != 0 and self.head.yspeed == 0:
                self.head.xspeed = 0

                if keys[pygame.K_UP]:
                    self.head.yspeed = -10
                else:
                    print("You lose!")
                    return True

            elif self.head.xspeed == 0 and self.head.yspeed != 0:
                self.head.yspeed = 0
                
                if keys[pygame.K_LEFT]:
                    self.head.xspeed = -10
                else:
                    print("You lose")
                    return True

        #CASE 5 - collide with left side and yspeed = 0 (horizontal)
        elif (self.head.x <= 0) and self.head.yspeed == 0: #if collided with left screen 
            self.head.xspeed = 0

            if keys[pygame.K_UP]:
                self.head.yspeed = -10
            elif keys[pygame.K_DOWN]:
                self.head.yspeed = 10
            else:
                print("You lose")
                return True

        #CASE 6 - collide with the left side and moving up or down
        elif (self.head.x <= 0) and self.head.yspeed != 0: 
            self.head.xspeed = 0

            if keys[pygame.K_LEFT]: #you collide (you lose)
                self.head.yspeed = 0
                print("You lose")
                return True


        #CASE 7 - you hit right side of screen (horizontal)
        elif (self.head.x >=  win.get_width() - self.head.width) and self.head.yspeed == 0:
            self.head.xspeed = 0
            
            if keys[pygame.K_UP]:
                self.head.yspeed = -10
            elif keys[pygame.K_DOWN]:
                self.head.yspeed = 10
            else:
                print("You lose")
                return True

        #CASE 8 - collide with the right side and moving up or down
        elif (self.head.x >= win.get_width() - self.head.width) and self.head.yspeed != 0: 
            self.head.xspeed = 0
            if keys[pygame.K_RIGHT]: #you collide (you lose)
                self.head.yspeed = 0
                print("You lose")
                return True



        #CASE 9 - collide with upper side and xspeed = 0 (vertical)
        elif (self.head.y <= 0) and self.head.xspeed == 0: 
            self.head.yspeed = 0

            if keys[pygame.K_LEFT]:
                self.head.xspeed = -10
            elif keys[pygame.K_RIGHT]:
                self.head.xspeed = 10
            else:
                print("You lose")
                return True 

        #CASE 10 - collide with the upper side and moving left or right
        elif (self.head.y <= 0) and self.head.xspeed != 0: 
            self.head.yspeed = 0

            if keys[pygame.K_UP]: #you collide (you lose)
                self.head.xspeed = 0
                print("You lose")
                return True

        #CASE 11 - collide with lower side and xspeed = 0 (vertical)
        elif (self.head.y >=  win.get_height() - self.head.height) and self.head.xspeed == 0: 
            self.head.yspeed = 0

            if keys[pygame.K_LEFT]:
                self.head.xspeed = -10
            elif keys[pygame.K_RIGHT]:
                self.head.xspeed = 10
            else:
                print("You lose")
                return True

        #CASE 12 - collide with the lower side and moving left or right
        elif (self.head.y >= win.get_height() - self.head.height) and self.head.xspeed != 0: 
            self.head.yspeed = 0

            if keys[pygame.K_DOWN]: #you collide (you lose)
                self.head.xspeed = 0
                print("You lose")
                return True
                
        return False