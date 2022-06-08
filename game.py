import pygame
from block import Block
from snake import Snake
from apple import Apple

pygame.init() #initialize pygame modules

#width and height of window     
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

#creating window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Colors used
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 15 #15 frames per second

#function to pause game and display paused screen (when 'p' is pressed)
def displayPausedScreen():
    """This function is to display the paused screen menu"""
    paused_font = pygame.font.SysFont('arial', 20)
    paused_surf = paused_font.render("Game is Paused! Please press 'p' again to continue", True, WHITE)
    screen.fill(BLACK)
    screen.blit(paused_surf, (10, 200))
    pygame.display.update()

    paused = True
    #main EVENT loop (this will run and handle everything related to the game)
    while paused:
        for event in pygame.event.get(): #get all the events in pygame
            if event.type == pygame.QUIT: #check if we quit the window (if we click the close button)
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                    break

#function to display when you win the game
def displayWinGameScreen():
    winning_font = pygame.font.SysFont('arial', 25)
    winning_surf = winning_font.render("Congratulations!! You won the game!", True, WHITE)
    screen.fill(BLACK)
    screen.blit(winning_surf, (100, 180))
    pygame.display.update()

    pygame.time.wait(3000) #wait 3 seconds

#function to display when game lost
def displayLostGameScreen():
    #create losing game  screen
    losing_font = pygame.font.SysFont('arial', 25)
    losing_surf = losing_font.render("YOU LOST!", True, WHITE)
    screen.fill(BLACK)
    screen.blit(losing_surf, (100, 180))
    pygame.display.update()
    
    global snake, apple
    #reinitialize snake and apple
    snake = Snake(100, 20, 10, 10) 
    apple = Apple(300, 20, 10, 10) 
    
    pygame.time.wait(3000) #wait 3 seconds




#Creating snake and apple object
#block = Block(20, 20, 10, 10)
snake = Snake(100, 20, 10, 10) 
apple = Apple(300, 20, 10, 10) 
#Adding window title
pygame.display.set_caption("Snake game            Snake Length: " + str(len(snake.blocks)))


clock = pygame.time.Clock()
running = True

#main game loop
while running:
    clock.tick(FPS)
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                displayPausedScreen()

    keys = pygame.key.get_pressed() #detect which keys were pressed
    
    #collision detection with walls and snake body
    if snake.detectCollisionWithWalls(screen):
        isGameOver = snake.handleCollisionWithWalls(keys, screen) #returns true if game is over
        if isGameOver:
           displayLostGameScreen() 

    if snake.detectCollisionIntoSelf():
        #game over screen here
        displayLostGameScreen()
        
    #if snake eats apple
    if snake.eatenApple(apple):
        apple = apple.generateNewApple(snake, screen) #make a new apple at a new position
        snake.growSnake() #increase snake length
        pygame.display.set_caption("Snake game            Snake Length: " + str(len(snake.blocks))) #change window title to display new snake length


    snake.moveSnake(keys, screen) #move snake

    #if snake occupies every space in window you win the game
    if len(snake.blocks) == (SCREEN_WIDTH * SCREEN_HEIGHT) // (snake.head.width ** 2): 
        displayWinGameScreen()

    #rendering objects onto screen
    screen.fill(BLACK)

    #block.drawBlock(screen)
    snake.drawSnake(screen)
    apple.drawApple(screen)

    #changing title of window
    pygame.display.set_caption("Snake game            Snake Length: " + str(len(snake.blocks)))
    pygame.display.update()


