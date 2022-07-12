import pygame
pygame.init()
import sys
import numpy
import game as gameLib
import player
import button
import menu as menuLib
import tkinter
from tkinter import Button
from tkinter.messagebox import askyesno
from tkinter import colorchooser
from tkinter import simpledialog

p1 = player.Player("Player 1", False, (255, 0, 0))
p2 = player.Player("Player 2", False, (255, 255, 0))
#Initialize Game
#fills every square on the board with an empty space
# Event Loop

    
    

menuLoop = True
appLoop = True
run = False
while appLoop:
    menu=menuLib.Menu()
    while menuLoop:
        for e in pygame.event.get():
            if menu.play_button.isClicked():
                print('START')
                menuLoop = False
                game = gameLib.Game(p1, p2)
                review = False
                run = True
                break
            if menu.exit_button.isClicked():
                menuLoop = False
                appLoop = False
                print('EXIT')
                break;
            if menu.setting_button.isClicked():
                print('SETTINGS')
                #Something something settings
                nn = simpledialog.askstring("Player 2 Nickame", "How should we call player 1?")
                color = colorchooser.askcolor(title ="Choose color for player 1")
                bot =  askyesno(title="Player 1", message="Is player 1 a bot?")
                diff = 0
                while bot:
                    diff = simpledialog.askstring("Bot Difficulty", "Easy medium or hard?")
                    match diff.lower():
                        case 'easy':
                            bot = False
                            diff = 1
                        case 'medium':
                            bot = False
                            diff = 2
                        case 'hard':
                            bot = False
                            diff = 3
                        case _:
                            bot = True
                            tkinter.messagebox.showinfo('Settings error', "Please pick an appropiate setting!")
                p1 = player.Player(nn, diff != 0, color[0], diff)
                nn = simpledialog.askstring("Player 2 Nickame", "How should we call player 2?")
                color = colorchooser.askcolor(title ="Choose color for player 2")
                
                bot =  askyesno(title="Player 2", message="Is player 2 a bot?")
                diff = 0
                while bot:
                    diff = simpledialog.askstring("Bot Difficulty", "Easy medium or hard?")
                    match diff.lower():
                        case 'easy':
                            bot = False
                            diff = 1
                        case 'medium':
                            bot = False
                            diff = 2
                        case 'hard':
                            bot = False
                            diff = 3
                        case _:
                            bot = True
                            tkinter.messagebox.showinfo('Settings error', "Please pick an appropiate setting!")
                p2 = player.Player(nn,diff != 0, color[0], diff)
                            
                    
                    
                
        

        pygame.display.update()
    menuLoop = True
    while run:
        # There is also event.get(), which returns an iterable of all events added to the queue during that iteration
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if game.click_btn1.isClicked():
                run, review = game.playTurn(0, run, review)
                
            if game.click_btn2.isClicked():
                run, review = game.playTurn(1, run, review)

            if game.click_btn3.isClicked():
                run, review = game.playTurn(2, run, review)

            if game.click_btn4.isClicked():
                run, review = game.playTurn(3, run, review)

            if game.click_btn5.isClicked():
                run, review = game.playTurn(4, run, review)

            if game.click_btn6.isClicked():
                run, review = game.playTurn(5, run, review)
    
            if game.click_btn7.isClicked():
                run, review = game.playTurn(6, run, review)

        if(game.players[game.turn - 1].isBot == True):
            run, review = game.playTurn(-1, run, review)


        if len(game.record) == 42 and run:
            print("Draw!")
            game.alert("Draw!")
            if not(game.askForReview()):
                run = False
            game.review(p1, p2, game.boardImage,game.record)
            review = True

        if(review == True):
            review = False
            reviewRecord = game.record.copy()
            index = 0
            while (run):
                    
                #print(repr(index) + ' ' + repr(len(reviewRecord)) )
                game.turn = index % 2 + 1
                game.reviewUpdate()
                    
                # There is also event.get(), which returns an iterable of all events added to the queue during that iteration
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        run = False
                    if game.click_btn5.isClicked():
                        if(index < len(reviewRecord)):
                            game.place(reviewRecord[index][1], True)
                            index += 1
                        else:
                            answer =  askyesno(title="Quit?", message="Out of moves. Would you like to quit?")
                            if answer:
                                run = False
                                review = False
                                menuLoop = True
                                break
                                
                            
                            
                    if game.click_btn3.isClicked():
                        if(index>=1):
                            index-=1
                            row = reviewRecord[index][0]
                            col = reviewRecord[index][1]
                            game.unplace(row,col)
                        else:
                            game.alert("no previous moves")


                    
                pygame.display.update()
                        


        pygame.display.update()


# When our main loop is no longer running, we want to stop execution
# Calling pygame.quit() before sys.exit() is best practice to avoid stalling
pygame.quit()
sys.exit()
print('we out')
