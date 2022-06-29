import pygame
import sys
import numpy
import game
import player
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

screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
screen.fill((255,255,255))
pygame.display.set_caption("CSE350 Team 10 Connect-4")
my_font = pygame.font.SysFont("monospace", 75)

#player vars
p1 = player.Player(False, (255, 0, 0))
p2 = player.Player(False, (255, 255, 0))

#Initialize Game
game = game.Game(p1, p2)
game.printBoard()

# Begin Event loop
run = True
while run:

    # There is also event.get(), which returns an iterable of all events added to the queue during that iteration
    for event in pygame.event.get():
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
