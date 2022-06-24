import pygame
import sys
import numpy
#Beginning Interfacte (Menu, butotns, etc) Kevin

#CheckWin  #CheckValid  #Place (update board variable)  Nikhil
#_Init__ -> Board Image for Game Alvin ??
#Update
#Player Stuff, brebones of cpu? Renz

#-> Testing Evniroment? Just using console? Aggeraget everything? mohammad
#alert? mohammad


#SCREEN STUFF
#Initialize all imported pygame modules (such as draw, sprite, etc.)

pygame.init()

# Constants for the screen
S_WIDTH = 640
S_HEIGHT = 640

# This method returns a pygame "surface" and acts as our window or display
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))

# Sets the caption of our window
pygame.display.set_caption("CSE350 Team 10 Connect-4")

my_font = pygame.font.SysFont("monospace", 75)

#Players to ask for input
#Also acts as CPU
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.Surface((25, 25))
        self.surface.fill((255, 0, 0))
        #self.surface = my_font.render("Hello", True, (255, 255, 255))
        self.rect = self.surface.get_rect(center=(S_WIDTH/2, S_HEIGHT/2))
    def move():
        
    def update(self, x, y):
        self.rect.move_ip(x, y)
class Game:
    #intializing variables
    board = numpy.zeros((6,7), int)
    record = []
    players = []
    #Intialize Board Variables, determine state of board?
    #Read variables, and create image of board
    
    def __init__(self, player1, player2, record):
        players = [player1, player2]
        
    #Update board image
    #reread board variable to update display
    #PYGAME LATER
    def update():

    #Ensures player puts a valid move
        
    def checkValid(column):


    #After valid placement, check for win by player
        
    def checkWin():
    
    #placing piece in appropiate column
    #Determinte playeer but using length(record) % 2 + 1 ??
    #Whoever does it will figure it out :)
        
    def place(column):

    #Create post-game menu
    def alert():

    #Starts review game
    def review():

    
        

#g = Game()

# Begin Event loop
run = True
while run:

    """Event handler"""
    #event = pygame.event.wait()  # This method returns the first element of an event queue, and pauses the screen if there are no events

    # There is also event.get(), which returns an iterable of all events added to the queue during that iteration
    for event in pygame.event.get():
    # Typical events include exiting the window via the X, or pressing the escape key
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            
            if event.key == pygame.K_LEFT:
                p1.update(-10, 0)
            if event.key == pygame.K_RIGHT:
                p1.update(10, 0)
            if event.key == pygame.K_UP:
                p1.update(0, -10)
            if event.key == pygame.K_DOWN:
                p1.update(0, 10)

    screen.fill((0,0,0))

    # pygame.draw.circle(screen, color=(255, 0, 0), center=(S_WIDTH/2, S_HEIGHT/2), radius=20)
    screen.blit(p1.surface, p1.rect)

    # Redraw the screen
    pygame.display.update()


# When our main loop is no longer running, we want to stop execution

# Calling pygame.quit() before sys.exit() is best practice to avoid stalling
pygame.quit()
sys.exit()
