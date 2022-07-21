from msilib import RadioButtonGroup
import pygame
pygame.init()
import sys
import numpy
import game as gameLib
import player
import button
import menu as menuLib
from tkinter import *
from tkinter import Button
from tkinter.messagebox import askyesno
from tkinter import colorchooser
from tkinter import simpledialog
import time

p1 = player.Player("Player 1", False, (255, 0, 0))
p2 = player.Player("Player 2", False, (255, 255, 0))
#Initialize Game
#fills every square on the board with an empty space
# Event Loop

    
    

menuLoop = True
appLoop = True
run = False


#Helper function for tkinter button
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb  

#Helper function for tkinter button
def updateColor(button, p):
    #Updates color of button
    button.configure(background=_from_rgb(p.color))


#Helper function for tkinter button
def updateText(button, p):
    #Updates text of button
    button.configure(text = ("Nickname = " + p.nickname))


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

                #Pop up Setting Menu
                Tk().withdraw()
                root = Toplevel()  
                   
                #Player 1 Header   
                l1 = Label(root, text = "Player 1")
                l1.grid(row=0, column=0)

                #Player 1 Nickname Button
                nameButton1 = Button(root, text = ("Nickname = " + p1.nickname), command=lambda: [p1.setName(), updateText(nameButton1, p1)], height = 1, width = 20)
                nameButton1.grid(row=1, column=0)

                
                #P1 Difficulty Radio Buttons 
                var1 = IntVar(root, p1.difficulty)
    
                Human1 = Radiobutton(root, text='Human', value=0, variable=var1, command=lambda value=0: p1.setBot(value))
                Easy1 = Radiobutton(root, text='Easy', value=1, variable=var1, command=lambda value=1: p1.setBot(value))
                Medium1 = Radiobutton(root, text='Medium', value=2, variable=var1, command=lambda value=2: p1.setBot(value))
                Hard1 = Radiobutton(root, text='Hard', value=3, variable=var1, command=lambda value=3: p1.setBot(value))
                Human1.grid(row=2, column=0)
                Easy1.grid(row=3, column=0)
                Medium1.grid(row=4, column=0)
                Hard1.grid(row=5, column=0)


                #P1 Color Button
                colorButton1 = Button(root, bg=_from_rgb(p1.color), text = "P1 Color", command=lambda: [p1.setColor(), updateColor(colorButton1, p1)], height = 1, width = 10)
                colorButton1.grid(row=6, column=0)


                #Player 2 Header
                l2 = Label(root, text = "Player 2")
                l2.grid(row=0, column=1)

                #Player 2 Nickname Button
                nameButton2 = Button(root, text = ("Nickname = " + p2.nickname), command=lambda: [p2.setName(), updateText(nameButton2, p2)], height = 1, width = 20)
                nameButton2.grid(row=1, column=1)


                #P2 Difficulty Radio Buttons
                var2 = IntVar(root, p2.difficulty)

                Human2 = Radiobutton(root, text='Human', value=0, variable=var2, command=lambda value=0: p2.setBot(value))
                Easy2 = Radiobutton(root, text='Easy', value=1, variable=var2, command=lambda value=1: p2.setBot(value))
                Medium2 = Radiobutton(root, text='Medium', value=2, variable=var2, command=lambda value=2: p2.setBot(value))
                Hard2 = Radiobutton(root, text='Hard', value=3, variable=var2, command=lambda value=3: p2.setBot(value))
                Human2.grid(row=2, column=1)
                Easy2.grid(row=3, column=1)
                Medium2.grid(row=4, column=1)
                Hard2.grid(row=5, column=1)

                

                #P2 Color Button
                colorButton2 = Button(root, bg=_from_rgb(p2.color), text = "P2 Color", command=lambda: [p2.setColor(), updateColor(colorButton2, p2)], height = 1, width = 10)
                colorButton2.grid(row=6, column=1)


                # root.mainloop()
                root.wait_window(root) 

                # try:
                #     root.after(1, root.quit)
                # except:
                #     pass

                
                print("exited settings")


                #Something something settings

                # nn = simpledialog.askstring("Player 2 Nickame", "How should we call player 1?")
                # color = colorchooser.askcolor(title ="Choose color for player 1")
                # bot =  askyesno(title="Player 1", message="Is player 1 a bot?")
                # diff = 0
                # while bot:
                #     diff = simpledialog.askstring("Bot Difficulty", "Easy medium or hard?")
                #     if diff is None:
                #         diff = 'easy'
                #     match diff.lower():
                #         case 'easy':
                #             bot = False
                #             diff = 1
                #         case 'medium':
                #             bot = False
                #             diff = 2
                #         case 'hard':
                #             bot = False
                #             diff = 3
                #         case _:
                #             bot = True
                #             tkinter.messagebox.showinfo('Settings error', "Please pick an appropiate setting!")
                # p1 = player.Player(nn, diff != 0, color[0], diff)
                # nn = simpledialog.askstring("Player 2 Nickame", "How should we call player 2?")
                # color = colorchooser.askcolor(title ="Choose color for player 2")
                
                # bot =  askyesno(title="Player 2", message="Is player 2 a bot?")
                # diff = 0
                # while bot:
                #     diff = simpledialog.askstring("Bot Difficulty", "Easy medium or hard?")
                #     if diff is None:
                #         diff = 'easy'
                #     match diff.lower():
                #         case 'easy':
                #             bot = False
                #             diff = 1
                #         case 'medium':
                #             bot = False
                #             diff = 2
                #         case 'hard':
                #             bot = False
                #             diff = 3
                #         case _:
                #             bot = True
                #             tkinter.messagebox.showinfo('Settings error', "Please pick an appropiate setting!")
                # p2 = player.Player(nn,diff != 0, color[0], diff)

        pygame.display.update()

    menuLoop = True
    
    #prevents mousedown from last menu to affect input
    prevent = 0
    while run:
        

        # There is also event.get(), which returns an iterable of all events added to the queue during that iteration
        for e in pygame.event.get():
            
            if e.type == pygame.MOUSEBUTTONUP:
                prevent = 1

            if e.type == pygame.QUIT:
                run = False
            if game.click_btn1.isClicked() and prevent == 1:
                run, review = game.playTurn(0, run, review)
                
            if game.click_btn2.isClicked() and prevent == 1:
                run, review = game.playTurn(1, run, review)

            if game.click_btn3.isClicked() and prevent == 1:
                run, review = game.playTurn(2, run, review)

            if game.click_btn4.isClicked() and prevent == 1:
                run, review = game.playTurn(3, run, review)

            if game.click_btn5.isClicked() and prevent == 1:
                run, review = game.playTurn(4, run, review)

            if game.click_btn6.isClicked() and prevent == 1:
                run, review = game.playTurn(5, run, review)
    
            if game.click_btn7.isClicked() and prevent == 1:
                run, review = game.playTurn(6, run, review)

        if(game.players[game.turn - 1].isBot == True):
            run, review = game.playTurn(-1, run, review)
            time.sleep(1)


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
