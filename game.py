import numpy as np
import player
import button
import pygame

from tkinter import messagebox

import tkinter 

from tkinter.messagebox import askyesno




class Game:
    
    
    #Read variables, and create image of board
    def __init__(self, player1, player2):
        self.S_WIDTH = 600
        self.S_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.S_WIDTH, self.S_HEIGHT))
        pygame.display.set_caption("CSE350 Team 10 Connect-4")
        my_font = pygame.font.SysFont("monospace", 75)
        self.tk = tkinter.Tk()
        self.tk.withdraw()
        self.record = []
        self.turn = 1
        self.board = np.zeros((6,7), dtype=int)
        self.players = [player1, player2]
        self.square = 80
        self.circleRad = 30
        self.B_WIDTH =self.square*7
        self.B_HEIGHT =self.square*6
        #Image
        self.boardTopLeft =((self.S_WIDTH - self.B_WIDTH)/2, self.S_HEIGHT - self.B_HEIGHT)
        self.boardImage = pygame.Surface((self.B_WIDTH, self.B_HEIGHT))
        self.boardImage.fill((0, 0, 255))
        self.clickImage = pygame.Surface((70, self.S_HEIGHT - 20))#-20 due to offset below
        self.clickImage.set_alpha(0)
        self.click_btn1 = button.Button(25, 20, self.clickImage)
        self.click_btn2 = button.Button(105, 20, self.clickImage)
        self.click_btn3 = button.Button(185, 20, self.clickImage)
        self.click_btn4 = button.Button(265, 20, self.clickImage)
        self.click_btn5 = button.Button(345, 20, self.clickImage)
        self.click_btn6 = button.Button(425, 20, self.clickImage)
        self.click_btn7 = button.Button(505, 20, self.clickImage)
        self.screen.fill((0,0,0))
        for r in range(6):
            for c in range(7):
                pygame.draw.circle(self.boardImage,
                                    (0, 0, 0),
                                    (self.square/2 + c * self.square, self.square/2 + r * self.square),
                                    self.circleRad)
        self.screen.blits(((self.boardImage, self.boardTopLeft), (self.clickImage, self.click_btn1.rect.topleft), 
                (self.clickImage, self.click_btn2.rect.topleft), (self.clickImage, self.click_btn3.rect.topleft), 
                (self.clickImage, self.click_btn4.rect.topleft), (self.clickImage, self.click_btn5.rect.topleft), 
                (self.clickImage, self.click_btn6.rect.topleft), (self.clickImage, self.click_btn7.rect.topleft)))

        
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


    def alert(self, message):

        messagebox.showinfo('Connect-Four', message)

        #tkinter.messagebox.showinfo('Connect-Four', message)


    def askForReview(self):
        answer = askyesno(title='Review Game?', message='Would you like to review this game?')
        if(answer):
            self.alert("review game...")
            return True
        return False
    def checkValid(self, column):
        if (self.board[5][column] == 0):
            #self.clearText(
            return False
        else:
            print("Invalid move")
            self.alert("Invalid Move")
            return True


    #assumes there is an open spot in the column, so always use self.checkValid() first
    def checkOpen(self, column):
        for i in range(6):
            if self.board[i][column] == 0:
                return i


    #placing piece in appropiate column, returns False if invalid column
    def place(self, col, review = False):
        #col = player.move()     #returns the column choice
        if self.checkValid(col):           #check if column is closed
            return False
        
        row = self.checkOpen(col)               #find earliest open row
        self.board[row][col] = self.turn        #place piece
        self.update(row, col, review)
        self.record.append((row, col))          #add move to the match record
        return True

    def unplace(self,r,c):
        self.board[r][c] = 0
        pygame.draw.circle(self.boardImage,
                    (0,0,0),
                    (self.square/2 + c * self.square, self.square/2 + (5-r) * self.square),
                    self.circleRad)

        pygame.display.update((self.S_WIDTH - self.B_WIDTH)/2 + c * self.square, (self.S_HEIGHT - self.B_HEIGHT) + (5-r) * self.square, self.square, self.square)
    #Redraws the board, interacting through the board variable and coloring in the circles
    def update(self, r, c, review = False):
        color = self.players[self.turn - 1].color
        pygame.draw.circle(self.boardImage,
                            color,
                            (self.square/2 + c * self.square, self.square/2 + (5-r) * self.square),
                            self.circleRad)
        if not review:
            #need this statement otherwise using place() causes use to recreate these buttons on the screen which is undesirable
            self.screen.blits(((self.boardImage, self.boardTopLeft), (self.clickImage, self.click_btn1.rect.topleft), 
                    (self.clickImage, self.click_btn2.rect.topleft), (self.clickImage, self.click_btn3.rect.topleft), 
                    (self.clickImage, self.click_btn4.rect.topleft), (self.clickImage, self.click_btn5.rect.topleft), 
                    (self.clickImage, self.click_btn6.rect.topleft), (self.clickImage, self.click_btn7.rect.topleft)))
        pygame.display.update((self.S_WIDTH - self.B_WIDTH)/2 + c * self.square, (self.S_HEIGHT - self.B_HEIGHT) + (5-r) * self.square, self.square, self.square)
    

    #Starts review game
    def review(self, player1, player2, record):
        self.clickImage = pygame.Surface((70, 100))
        self.clickImage.fill((255, 255, 255))
        #fills every square on the board with an empty space
        for r in range(6):
            for c in range(7):
                pygame.draw.circle(self.boardImage,
                                    (0, 0, 0),
                                    (self.square/2 + c * self.square, self.square/2 + r *self.square),
                                    self.circleRad)
        self.turn = 1
        self.board = np.zeros((6,7), dtype=int)
        self.players = [player1, player2]
        self.square = 80
        self.circleRad = 30
        self.B_WIDTH =self.square*7
        self.B_HEIGHT =self.square*6
    def reviewUpdate(self):
        self.screen.fill((0,0,0))
        self.screen.blits(((self.boardImage, self.boardTopLeft), (self.clickImage, self.click_btn3.rect.topleft), 
                 (self.clickImage, self.click_btn5.rect.topleft)))
    def playTurn(self, col, run, review):
        if col == -1: #bot case
            col = self.players[self.turn - 1].move(self.turn, self.board)
        self.place(col)
        if self.checkWin():
            print(f"{self.players[self.turn - 1].nickname} Wins!")
            self.alert(f"{self.players[self.turn - 1].nickname} Wins!")
            if not(self.askForReview()):
                 run = False
            self.review(self.players[0], self.players[1],self.record)
            review = True
        return run, review

    
