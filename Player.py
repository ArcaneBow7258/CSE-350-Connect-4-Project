import random
import math

class Player:

    def __init__(self, isBot, color, difficulty=0):
        #color input should be a variable in the format of (###,###,###)
        self.isBot = isBot
        self.color = color
        self.difficulty = difficulty
        self.score = 0


    def evaluate_window(self, window, piece):
        score = 0
        

        #DETERMINE OPPONENT'S PIECE
        if(piece == 1):
            opp_piece = 2
        else:
            opp_piece = 1

        #DETERMINE SCORE OF BOARD POSITIONS
        if(window.count(piece) == 4):
            score += 100

        elif(window.count(piece) == 3 and window.count(0) == 1):
            score += 5

        elif(window.count(piece) == 2 and window.count(0) == 2):
            score += 2
        
        elif(window.count(opp_piece) == 3 and window.count(0) == 1):
            score -= 4
        
        else:
            pass

        return score
            
        

    def score_position(self, board, turn):
        score = 0

        ## Score center column
        center_array = [int(i) for i in list(board[:, 7//2])]
        center_count = center_array.count(turn)
        score += center_count * 3

        ##Score Horizontal
        for r in range(6):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(4):
                window = row_array[c:c+4]
                score += self.evaluate_window(window, turn)

        ## Score Vertical
        for c in range(7):
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(3):
                window = col_array[r:r+4]
                score += self.evaluate_window(window, turn)

        ## Score negaive sloped diagonal
        for r in range(3):
            for c in range(4):
                window = [board[r+i][c+i] for i in range(4)]
                score += self.evaluate_window(window, turn)

        ## Score posiive sloped diagonal
        for r in range(3):
            for c in range(4):
                window = [board[r+3-i][c+i] for i in range(4)]
                score += self.evaluate_window(window, turn)

        return score


    def is_valid_location(self, board, column):
        ##CHECK IF TOP ROW IS OPEN
        if (board[0][column] == 0):
            return True
        else:
            return False

    def winning_move(self, turn):
        chip = turn

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
        
        return False


    def get_valid_locations(self, board):
        ##GET LIST OF OPEN COLUMNS
        valid_locations = []
        for col in range(7):
            if(self.is_valid_location(board, col)):
                valid_locations.append(col)
        return valid_locations


    def is_terminal_node(self, board, piece):
        #DETERMINE OPPONENT'S PIECE
        if(piece == 1):
            opp_piece = 2
        else:
            opp_piece = 1
        
        #TERMINAL NODE IF WINNING MOVE OR DRAW
        return self.winning_move(board, piece) \
            or self.winning_move(board, opp_piece) \
            or len(self.get_valid_locations(board)) == 0

    def get_next_open_row(self, board, col):
        for r in range(6):
            if(board[r][col] == 0):
                return r
            else:
                pass

    def drop_piece(self, board, col, turn):
            
        row = self.get_next_open_row(col)  #find earliest open row
        board[row][col] = self.turn        #place piece

        return board


    def minimax(self, board, depth, alpha, beta, maximizingPlayer, AI, OPP): #AI = cpu turn number, #OPP = opp turn #
        valid_locations = self.get_valid_locations(board)
        is_terminal = self.is_terminal_node(board)

        if depth == 0 or is_terminal:
            if is_terminal:
                if self.winning_move(board, AI):
                    return (None, 100000000000000)
                elif self.winning_move(board, OPP):
                    return (None, -10000000000000)
                else: # Game is over, no more valid moves
                    return (None, 0)
            else: # Depth is zero  
                return (None, self.score_position(board, AI))

        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                b_copy = board.copy()
                self.drop_piece(b_copy, col, AI)
                new_score = self.minimax(b_copy, depth-1, alpha, beta, False, AI, OPP)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else: # Minimizing player
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                b_copy = board.copy()
                self.drop_piece(b_copy, col, OPP)
                new_score = self.minimax(b_copy, depth-1, alpha, beta, True, AI, OPP)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value
            

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
            while action1:
                col = int(input("Enter column to place(1-7): ")) - 1
                if col in [0, 1, 2, 3, 4, 5, 6]:
                    action1 = False
            return col