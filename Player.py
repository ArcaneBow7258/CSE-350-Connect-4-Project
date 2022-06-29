import random
#next test

class Player:

    def __init__(self, isBot, color, difficulty=0):     #color input should be a variable in the format of (###,###,###)
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
            action1 = True
            col = -1
            while action1:
                try:
                    col = int(input("Enter column to place(1-7): ")) - 1
                    if col in [0, 1, 2, 3, 4, 5, 6]:
                        action1 = False
                except:
                    action1 = True
            return col
