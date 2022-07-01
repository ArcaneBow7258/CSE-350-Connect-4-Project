import random
import button
#3rd test

class Player:

    def __init__(self, nickname, isBot, color, difficulty=0):     #color input should be a variable in the format of (###,###,###)
        self.nickname = nickname
        self.isBot = isBot
        self.color = color
        self.difficulty = difficulty
        

    def move(self):
        if(self.isBot):
            match self.difficulty:  #Potentially pass in a list of available columns to optimize
                case 1:
                    col = random.randrange(1,7)
                    return col
                case 2:
                    return 0    #Will use min/max algo
                case 3:
                    return 0    #will use min/max algo
        
        else:   #This function probably changes for human when we have a GUI (based on position on screen)
            for e in pygame.event.get():
                if click_btn1.isClicked():
                    return 0
                if click_btn2.isClicked():
                    return 1
                if click_btn3.isClicked():
                    return 2
                if click_btn4.isClicked():
                    return 3
                if click_btn5.isClicked():
                    return 4
                if click_btn6.isClicked():
                    return 5
                if click_btn7.isClicked():
                    return 6
