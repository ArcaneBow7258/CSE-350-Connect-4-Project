import numpy as np
import player
import button
import pygame
#pygame.init()
class Game:
    #Read variables, and create image of board
    def __init__(self, player1, player2):
        self.record = []
        self.turn = 1
        self.board = np.zeros((6,7), dtype=int)
        self.players = [player1, player2]
        self.square = 80
        self.circleRad = 30
        self.B_WIDTH =self.square*7
        self.B_HEIGHT =self.square*6


    #prints the board
    def printBoard(self):
        print(np.flip(self.board, 0))


    #After valid placement, check for win by player
    def checkWin(self):
        chip = self.turn

        #horizontal check
        for c in range(4):
            for r in range(6):
                if self.board[r][c] == chip and self.board[r][c+1] == chip and self.board[r][c+2] == chip and self.board[r][c+3] == chip:
                    return True
        
        #vertical check
        for c in range(7):
            for r in range(3):
                if self.board[r][c] == chip and self.board[r+1][c] == chip and self.board[r+2][c] == chip and self.board[r+3][c] == chip:
                    return True
        
        #upward diagonal check
        for c in range(4):
            for r in range(3):
                if self.board[r][c] == chip and self.board[r+1][c+1] == chip and self.board[r+2][c+2] == chip and self.board[r+3][c+3] == chip:
                    return True
        
        #downward diagonal check
        for c in range(3,7):
            for r in range(3):
                if self.board[r][c] == chip and self.board[r+1][c-1] == chip and self.board[r+2][c-2] == chip and self.board[r+3][c-3] == chip:
                    return True
        
        self.turn = len(self.record) % 2 + 1    #update turn value
        return False


    def alert(self):
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("Invalid move", True, (255,0,0), (255,255,255))
        textRect = text.get_rect()
        textRect.center=(S_WIDTH/2, S_HEIGHT-100)
        screen.blit(text, textRect)
        pygame.display.update()


    def clearText(self):
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("Invalid move", True, (255,255,255), (255,255,255))
        textRect = text.get_rect()
        textRect.center=(S_WIDTH/2, S_HEIGHT-100)
        screen.blit(text, textRect)
        pygame.display.update()


        #Ensures player puts a valid move
    def checkValid(self, column):
        if (self.board[5][column] == 0):
            #self.clearText()
            return False
        else:
            print("Invalid move")
            #self.alert()
            return True


    #assumes there is an open spot in the column, so always use self.checkValid() first
    def checkOpen(self, column):
        for i in range(6):
            if self.board[i][column] == 0:
                return i


    #placing piece in appropiate column, returns False if invalid column
    def place(self, player):
        col = player.move()     #player's choice of column
            
        if self.checkValid(col):           #check if column is closed
            return False
        
        row = self.checkOpen(col)               #find earliest open row
        self.board[row][col] = self.turn        #place piece
        self.update(row, col)
        self.record.append((row, col))          #add move to the match record
        
        return True


    #Redraws the board, interacting through the board variable and coloring in the circles
    def update(self, r, c):
        color = self.players[self.turn - 1].color
        pygame.draw.circle(self.boardImage,
                            color,
                            (self.square/2 + c * self.square, self.square/2 + (5-r) * self.square),
                            self.circleRad)

        pygame.display.update((S_WIDTH - self.B_WIDTH)/2 + c * self.square, (S_HEIGHT - self.B_HEIGHT) + (5-r) * self.square, self.square, self.square)
    

    #Starts review game
    def review():
        pass