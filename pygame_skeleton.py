import pygame
import sys
import numpy
import game
import player
import button
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

S_WIDTH = 600
S_HEIGHT = 600
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("CSE350 Team 10 Connect-4")
my_font = pygame.font.SysFont("monospace", 75)

#player vars
p1 = player.Player(False, (255, 0, 0))
p2 = player.Player(False, (255, 255, 0))

#Initialize Game
game = game.Game(p1, p2)

boardTopLeft =((S_WIDTH - game.B_WIDTH)/2, S_HEIGHT - game.B_HEIGHT)
boardImage = pygame.Surface((game.B_WIDTH, game.B_HEIGHT))
boardImage.fill((0, 0, 255))
clickImage = pygame.Surface((60, 80))
clickImage.fill((255, 255, 255))
click_btn1 = button.Button(0, 0, clickImage)
click_btn2 = button.Button(70, 0, clickImage)
click_btn3 = button.Button(140, 0, clickImage)
click_btn4 = button.Button(210, 0, clickImage)
click_btn5 = button.Button(280, 0, clickImage)
click_btn6 = button.Button(350, 0, clickImage)
click_btn7 = button.Button(420, 0, clickImage)

#fills every square on the board with an empty space
for r in range(6):
    for c in range(7):
        pygame.draw.circle(boardImage,
                            (0, 0, 0),
                            (game.square/2 + c * game.square, game.square/2 + r * game.square),
                            game.circleRad)

# Begin Event loop
run = True
while run:

    screen.fill((0,0,0))

    screen.blits(((boardImage, boardTopLeft), (clickImage, click_btn1.rect.topleft), 
                (clickImage, click_btn2.rect.topleft), (clickImage, click_btn3.rect.topleft), 
                (clickImage, click_btn4.rect.topleft), (clickImage, click_btn5.rect.topleft), 
                (clickImage, click_btn6.rect.topleft), (clickImage, click_btn7.rect.topleft)))

    if click_btn1.isClicked():
        print(1)
    if click_btn2.isClicked():
        print(2)
    if click_btn3.isClicked():
        print(3)
    if click_btn4.isClicked():
        print(4)
    if click_btn5.isClicked():
        print(5)
    if click_btn6.isClicked():
        print(6)
    if click_btn7.isClicked():
        print(7)


    
    # There is also event.get(), which returns an iterable of all events added to the queue during that iteration
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    pygame.display.update()

# When our main loop is no longer running, we want to stop execution

# Calling pygame.quit() before sys.exit() is best practice to avoid stalling
pygame.quit()
sys.exit()
