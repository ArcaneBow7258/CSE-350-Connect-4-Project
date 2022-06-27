import numpy as np
import player

class Game:
    #intializing variables
    record = []
    players = []
    turn = 1


    #Intialize Board Variables, determine state of board?
    #Read variables, and create image of board
    def __init__(self):
        self.board = np.zeros((6,7), dtype=int)

    def printBoard(self):
        print(np.flip(self.board, 0))

    #Ensures player puts a valid move
    def checkValid(self, column):
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
    def checkWin(self, chip):
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
        
        #positive diagonal check
        for c in range(4):
            for r in range(3):
                if self.board[r][c] == chip and self.board[r+1][c+1] == chip and self.board[r+2][c+2] == chip and self.board[r+3][c+3] == chip:
                    return True
        
        #negative diagonal check
        for c in range(4):
            for r in range(3, 6):
                if self.board[r][c] == chip and self.board[r-1][c-1] == chip and self.board[r-2][c-2] == chip and self.board[r-3][c-3] == chip:
                    return True
        
        self.turn = len(self.record) % 2 + 1    #update turn value
        return False

    #placing piece in appropiate column, returns False if invalid column
    def place(self, player, chip):
        col = player.move()     #player's choice of column
            
        if self.checkValid(col):           #check if column is closed
            return False
        
        row = self.checkOpen(col)               #find earliest open row
        self.board[row][col] = chip             #"insert" piece
        self.printBoard()                       #print board
        self.record.append((row, col))          #add move to the match record
        return True

    #Create post-game menu
    def alert():
        pass

    #Starts review game
    def review():
        pass
    

game = Game()
p1 = player.Player(False, (255, 0, 0))
p2 = player.Player(False, (0, 0, 255))
game.printBoard()
run = True
for i in range(21):
    while game.turn == 1:
        chip = 1
        game.place(p1, chip)
        if game.checkWin(chip):
            print("Player 1 Wins!")
            break
    while game.turn == 2:
        chip = 2
        game.place(p2, chip)
        if game.checkWin(chip):
            print("Player 2 Wins!")
            break