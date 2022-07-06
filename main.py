import pygame
import sys
import numpy
import game
import player
import button

#SCREEN STUFF
pygame.init()

S_WIDTH = 600
S_HEIGHT = 600
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("CSE350 Team 10 Connect-4")
my_font = pygame.font.SysFont("monospace", 75)

#player vars
p1 = player.Player("Player 1", False, (255, 0, 0))
p2 = player.Player("Player 2", False, (255, 255, 0))

#Initialize Game
game = game.Game(p1, p2)

boardTopLeft =((S_WIDTH - game.B_WIDTH)/2, S_HEIGHT - game.B_HEIGHT)
boardImage = pygame.Surface((game.B_WIDTH, game.B_HEIGHT))
boardImage.fill((0, 0, 255))
clickImage = pygame.Surface((70, 100))
clickImage.fill((255, 255, 255))
click_btn1 = button.Button(25, 20, clickImage)
click_btn2 = button.Button(105, 20, clickImage)
click_btn3 = button.Button(185, 20, clickImage)
click_btn4 = button.Button(265, 20, clickImage)
click_btn5 = button.Button(345, 20, clickImage)
click_btn6 = button.Button(425, 20, clickImage)
click_btn7 = button.Button(505, 20, clickImage)

#fills every square on the board with an empty space
for r in range(6):
    for c in range(7):
        pygame.draw.circle(boardImage,
                            (0, 0, 0),
                            (game.square/2 + c * game.square, game.square/2 + r * game.square),
                            game.circleRad)

# Begin Event loop
review = False
run = True
while run:
    
        

    screen.fill((0,0,0))

    screen.blits(((boardImage, boardTopLeft), (clickImage, click_btn1.rect.topleft), 
                (clickImage, click_btn2.rect.topleft), (clickImage, click_btn3.rect.topleft), 
                (clickImage, click_btn4.rect.topleft), (clickImage, click_btn5.rect.topleft), 
                (clickImage, click_btn6.rect.topleft), (clickImage, click_btn7.rect.topleft)))
    
    # There is also event.get(), which returns an iterable of all events added to the queue during that iteration
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    
        if click_btn1.isClicked():
            game.place(0, boardImage)
            if game.checkWin():
                print(f"{game.players[game.turn - 1].nickname} Wins!")
                game.alert(f"{game.players[game.turn - 1].nickname} Wins!")
                if not(game.askForReview()):
                    run = False
                game.review(p1, p2, boardImage,game.record)
                review = True

        if click_btn2.isClicked():
            game.place(1, boardImage)
            if game.checkWin():
                print(f"{game.players[game.turn - 1].nickname} Wins!")
                game.alert(f"{game.players[game.turn - 1].nickname} Wins!")
                if not(game.askForReview()):
                    run = False
                game.review(p1, p2, boardImage,game.record)
                review = True
                

        if click_btn3.isClicked():
            game.place(2, boardImage)
            if game.checkWin():
                print(f"{game.players[game.turn - 1].nickname} Wins!")
                game.alert(f"{game.players[game.turn - 1].nickname} Wins!")
                if not(game.askForReview()):
                    run = False
                game.review(p1, p2, boardImage,game.record)
                review = True

        if click_btn4.isClicked():
            game.place(3, boardImage)
            if game.checkWin():
                print(f"{game.players[game.turn - 1].nickname} Wins!")
                game.alert(f"{game.players[game.turn - 1].nickname} Wins!")
                if not(game.askForReview()):
                    run = False
                game.review(p1, p2, boardImage,game.record)
                review = True

        if click_btn5.isClicked():
            game.place(4, boardImage)
            if game.checkWin():
                print(f"{game.players[game.turn - 1].nickname} Wins!")
                game.alert(f"{game.players[game.turn - 1].nickname} Wins!")
                if not(game.askForReview()):
                    run = False
                game.review(p1, p2, boardImage,game.record)
                review = True

        if click_btn6.isClicked():
            game.place(5, boardImage)
            if game.checkWin():
                print(f"{game.players[game.turn - 1].nickname} Wins!")
                game.alert(f"{game.players[game.turn - 1].nickname} Wins!")
                if not(game.askForReview()):
                    run = False
                game.review(p1, p2, boardImage,game.record)
                review = True

        if click_btn7.isClicked():
            game.place(6, boardImage)
            if game.checkWin():
                print(f"{game.players[game.turn - 1].nickname} Wins!")
                game.alert(f"{game.players[game.turn - 1].nickname} Wins!")
                if not(game.askForReview()):
                    run = False
                game.review(p1, p2, boardImage,game.record)
                review = True
    
    if len(game.record) == 42 and run:
        print("Draw!")
        game.alert("Draw!")
        if not(game.askForReview()):
            run = False
        game.review(p1, p2, boardImage,game.record)
        review = True

    if(review == True):
        review = False
        reviewRecord = game.record.copy()
        index = 0
        while (run):
            print(repr(index) + ' ' + repr(len(reviewRecord)) )
            game.turn = index % 2 + 1
            screen.fill((0,0,0))

            screen.blits(((boardImage, boardTopLeft), (clickImage, click_btn3.rect.topleft), 
                        (clickImage, click_btn5.rect.topleft)))
            
            # There is also event.get(), which returns an iterable of all events added to the queue during that iteration
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False
            if click_btn5.isClicked():
                if(index < len(reviewRecord)):
                    game.place(reviewRecord[index][1], boardImage)
                    index += 1
                else:
                    game.alert("no more moves")
            if click_btn3.isClicked():
                if(index>=1):
                    index-=1
                    row = reviewRecord[index][0]
                    col = reviewRecord[index][1]
                    game.board[row][col] = 0
                    pygame.draw.circle(boardImage,
                            (0,0,0),
                            (game.square/2 + col * game.square, game.square/2 + (5-row) * game.square),
                            game.circleRad)

                    pygame.display.update((S_WIDTH - game.B_WIDTH)/2 + c * game.square, (S_HEIGHT - game.B_HEIGHT) + (5-row) * game.square, game.square, game.square)
                else:
                    game.alert("no previous moves")


            
            pygame.display.update()
                


    pygame.display.update()

# When our main loop is no longer running, we want to stop execution

# Calling pygame.quit() before sys.exit() is best practice to avoid stalling
pygame.quit()
sys.exit()
