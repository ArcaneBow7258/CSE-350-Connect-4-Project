
import random
#Using pygui to get input
class Player:

    def __init__(self, isBot, color, difficulty=0):
        #color input should be a variable in the format of (###,###,###)
        self.isBot = isBot
        self.color = color
        self.difficulty = difficulty
        

    def move(self):
        if(self.isBot):
             match self.difficulty:
                #Potentially pass in a list of available columns to optimize
                case 1:
                    col = random.randrange(1,7)
                    return col
                case 2:
                    #Will use min/max algo
                    return 0
                case 3:
                    #will use min/max algo
                    return 0
        
        else:
            #This function probably changes for human when we have a GUI (based on position on screen)
            col = input("Enter column to place: ")
            return col
