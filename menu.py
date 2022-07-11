import numpy
import pygame
import button

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('CONNECT 4 MENU')

play_img = pygame.image.load('playbutton.png').convert_alpha()
exit_img = pygame.image.load('exitbutton.png').convert_alpha()
setting_img = pygame.image.load('settingsbutton.png').convert_alpha()
connect_img = pygame.image.load('connect4.png').convert_alpha()

#create button instances
connect_button = button.Button(100, 0, connect_img, 0.3)
play_button = button.Button(120, 195, play_img, 0.5)
exit_button = button.Button(500, 200, exit_img, 0.5)
setting_button = button.Button(300, 300, setting_img, 0.5)

#game loop
run = True
while run:

    screen.fill((202, 228, 241))

    connect_button.draw(screen)
    if play_button.draw(screen):
        print('START')
    if exit_button.draw(screen):
        run = False
        #print('EXIT')
    if setting_button.draw(screen):
        print('SETTINGS')

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()
        
pygame.quit()
