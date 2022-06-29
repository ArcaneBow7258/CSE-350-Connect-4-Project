import numpy as np
import player
#import player
import pygame
pygame.init()
S_WIDTH = 720
S_HEIGHT = 720
class Game:
    #intializing variables
    record = []
    players = []
    turn = 1
    board = np.zeros((6,7), dtype=int)
    square = 80
    circleRad = 30
    B_WIDTH =square*7
    B_HEIGHT =square*6
    boardOffset =(S_WIDTH - B_WIDTH)/2
    boardImage = pygame.Surface((B_WIDTH, B_HEIGHT))
    boardImage.fill((0, 0, 255))
    
    #Intialize Board Variables, determine state of board?
    #Read variables, and create image of board
    def __init__(self, player1, player2):
        self.board = np.zeros((6,7), dtype=int)
        self.players = [player1, player2]
        
        
        #Creating Screen for board
        
        
        
        self.reDraw()
        
        pygame.display.update()
    def printBoard(self):
        print(np.flip(self.board, 0))

    #Ensures player puts a valid move
    def checkValid(self, column):
        print(type(column))
        if (self.board[5][column] == 0):
            return False
        else:
            print("Invalid move")
            return True

    #assumes there is an open spot in the column, so always use self.checkValid() first
    def checkOpen(self, column):
        for i in range(6):
            if self.board[i][column] == 0:
                return i


    #After valid placement, check for win by player
    def checkWin(self):
        chip = self.turn
        print(self.board)
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

    #placing piece in appropiate column, returns False if invalid column
    def place(self, player):
        col = player.move()     #player's choice of column
            
        if self.checkValid(col):           #check if column is closed
            return False
        
        row = self.checkOpen(col)               #find earliest open row
        self.board[row][col] = self.turn        #place piece
        self.printBoard()                       #print board
        self.reDraw()
        self.record.append((row, col))          #add move to the match record
        
        return True
    #Redraws the board, interating through the board variable and coloring in the circles
    def reDraw(self):
        b = np.flip(self.board, 0)
        self.boardImage.fill((0, 0, 255))
        for r in range(0,6):
            for c in range(0,7):
                chip =  b[r][c] - 1
    
                color = self.players[b[r][c] - 1].color if chip != -1 else (255, 255, 255)
                c = pygame.draw.circle(self.boardImage,
                                       color,
                                       ((self.square - self.circleRad*2)/2 +self.circleRad  + c * self.square, (self.square)/2 + r * self.square),
                                       self.circleRad)
                
        screen.blit(self.boardImage, (self.boardOffset,0))
        pygame.display.update()

    #Create post-game menu
    def alert():
        pass

    #Starts review game
    def review():
        pass

#Beginning image? menu?
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
screen.fill((255,255,255))
pygame.display.set_caption("CSE350 Team 10 Connect-4")
my_font = pygame.font.SysFont("monospace", 75)

#player vars
p1 = player.Player(False, (255, 0, 0))
p2 = player.Player(False, (255, 255, 0))

#Initialize Game
game = Game(p1, p2)
game.printBoard()

rune = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pvpGame = True
    while pvpGame:
        pygame.event.get()
        while game.turn == 1:
            game.place(p1)
            pygame.display.update()
            if game.checkWin():
                print("Player 1 Wins!")
                pvpGame = False
                break
        while game.turn == 2:
            game.place(p2)
            pygame.display.update()
            if game.checkWin():
                print("Player 2 Wins!")
                pvpGame = False
                break
        if len(game.record) == 42 and pvpGame:
            print("Draw!")
            pvpGame = False
pygame.quit()