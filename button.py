import pygame

class Button():
    def __init__(self, x, y, image):
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def isClicked(self):
        action = False

        #mouse position
        pos = pygame.mouse.get_pos()

        #check click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        if pygame.mouse.get_pressed()[0]:
            self.clicked = True
        return action

