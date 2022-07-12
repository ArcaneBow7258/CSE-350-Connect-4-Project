import numpy
import pygame
import button
import os
#create display window

class Menu:
    def __init__(self):
        
        MENU_HEIGHT = 500
        MENU_WIDTH = 800
        self.screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
        pygame.display.set_caption('CONNECT 4 MENU')

        play_img = pygame.image.load(os.path.join('images','playbutton.png')).convert_alpha()
        exit_img = pygame.image.load(os.path.join('images','exitbutton.png')).convert_alpha()
        setting_img = pygame.image.load(os.path.join('images','settingsbutton.png')).convert_alpha()
        connect_img = pygame.image.load(os.path.join('images','connect4.png')).convert_alpha()
        
        play_img = pygame.transform.scale(play_img, (int(play_img.get_rect()[2] * 0.5), int(play_img.get_rect()[3] * 0.5)))
        exit_img = pygame.transform.scale(exit_img, (int(exit_img.get_rect()[2] * 0.5), int(exit_img.get_rect()[3] * 0.5)))
        setting_img = pygame.transform.scale(setting_img, (int(setting_img.get_rect()[2] * 0.5), int(setting_img.get_rect()[3] * 0.5)))
        connect_img = pygame.transform.scale(connect_img, (int(connect_img.get_rect()[2] * 0.3), int(connect_img.get_rect()[3] * 0.3)))
        
        play_img.set_colorkey((255,255,255))
        exit_img.set_colorkey((255,255,255))
        setting_img.set_colorkey((255,255,255))
        connect_img.set_colorkey((255,255,255))
        #create button instances
        self.connect_button = button.Button(100, 0, connect_img)
        self.play_button = button.Button(120, 195, play_img)
        self.exit_button = button.Button(500, 200, exit_img)
        self.setting_button = button.Button(300, 300, setting_img)

        self.screen.fill((202, 228, 241))

        self.screen.blits((
            (connect_img, self.connect_button.rect.topleft),
            (play_img, self.play_button.rect.topleft),
            (exit_img, self.exit_button.rect.topleft),
            (setting_img, self.setting_button.rect.topleft)
        ))
        pygame.display.update()
    def close(self):
        self.screen.quit()
