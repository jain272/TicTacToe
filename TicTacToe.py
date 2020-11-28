# This program allows the user to select either a 1-player or 2-player
# Tic-Tac-Toe game in a graphical user interface. The 1-player is played
# by an AI while the 2-player allows the user to play with a friend. 

import time
from graphics import *

#This function creates the initial control panel with a splash screen
def create():
    splashS = GraphWin("Control Panel", 400, 400)
    splashS.setBackground("lightgrey")
    titleImg = Image(Point(200, 50), "TicTacToe-Title.gif")
    label1 = Text(Point(200, 125), "v2.0")
    label1.setSize(14)
    Img2 = Image(Point(200, 270), "TicTacToe-Board.gif")
    titleImg.draw(splashS)
    label1.draw(splashS)
    Img2.draw(splashS)
    time.sleep(3)
    Img2.undraw()
    Button1 = Oval(Point(50, 200), Point(180, 250))
    Button1.setFill("green")
    Button2 = Oval(Point(200, 200), Point(330, 250))
    Button2.setFill("blue")
    Button1.draw(splashS)
    Button2.draw(splashS)
    Button3 = Rectangle(Point(115, 300), Point(265, 350))
    Button3.setFill("red")
    Button3.draw(splashS)
    label2 = Text(Button1.getCenter(), "1-Player")
    label3 = Text(Button2.getCenter(), "2-Player")
    label4 = Text(Button3.getCenter(), "EXIT")
    label2.setSize(18)
    label3.setSize(18)
    label4.setSize(18)
    label2.setFill("white")
    label3.setFill("white")
    label4.setFill("white")
    label2.draw(splashS)
    label3.draw(splashS)
    label4.draw(splashS)
    return splashS, Button1, Button2, Button3

#This function has the tic tac toe board with the game logic
def board(numPlayers):
    board = GraphWin("Game Board", 600, 600)
    VerLine1 = Line(Point(220, 100), Point(220, 500))
    VerLine2 = Line(Point(380, 100), Point(380, 500))
    HorLine1 = Line(Point(100, 220), Point(500, 220))
    HorLine2 = Line(Point(100, 380), Point(500, 380))
    VerLine1.setWidth(3)
    VerLine2.setWidth(3)
    HorLine1.setWidth(3)
    HorLine2.setWidth(3)
    VerLine1.draw(board)
    VerLine2.draw(board)
    HorLine1.draw(board)
    HorLine2.draw(board)
    if (numPlayers == 2):
        # 2 Player game logic
        labelT = Text(Point(300, 50), "Your turn Player 1")
        labelT.setSize(24)
        labelT.draw(board)
        labelB = Text(Point(300, 550), "Click to place a marker")
        labelB.setSize(24)
        labelB.draw(board)
    elif (numPlayers == 1):
        labelT = Text(Point(300, 50), "My turn")
        labelB = Text(Point(300, 550), "Thinking...")
        labelT.setSize(24)
        labelB.setSize(24)
        labelB.draw(board)
        labelT.draw(board)

    plays = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    flag = 1
    for i in range (0,9):
        click = board.getMouse()
        if (click.getX() > 100 and click.getX() < 220 and click.getY() > 100 and click.getY() < 220):
            if (i % 2 == 0):
                line1 = Line(Point(120, 120), Point(200, 200))
                line1.setWidth(2)
                line1.draw(board)
                line2 = Line(Point(200, 120), Point(120, 200))
                line2.setWidth(2)
                line2.draw(board)
                plays[0] = 'X'
                labelT.setText("Your turn Player 2")
            else:
                circle = Circle(Point(160, 160), 45)
                circle.setWidth(2)
                if (plays[0] == ' '):
                    circle.draw(board)
                    plays[0] = 'O'
                    labelT.setText("Your turn Player 1")
        elif (click.getX() > 100 and click.getX() < 220 and click.getY() > 220 and click.getY() < 380):
            if (i % 2 == 0):
                line1 = Line(Point(120, 240), Point(200, 360))
                line1.setWidth(2)
                line1.draw(board)
                line2 = Line(Point(200, 240), Point(120, 360))
                line2.setWidth(2)
                line2.draw(board)
                plays[3] = 'X'
                labelT.setText("Your turn Player 2")
            else:
                circle = Circle(Point(160, 300), 45)
                circle.setWidth(2)
                if (plays[3] == ' '):
                    circle.draw(board)
                    plays[3] = 'O'
                    labelT.setText("Your turn Player 1")
        elif (click.getX() > 100 and click.getX() < 220 and click.getY() > 380 and click.getY() < 500):
            if (i % 2 == 0):
                line1 = Line(Point(120, 400), Point(200, 480))
                line1.setWidth(2)
                line1.draw(board)
                line2 = Line(Point(200, 400), Point(120, 480))
                line2.setWidth(2)
                line2.draw(board)
                plays[6] = 'X'
                labelT.setText("Your turn Player 2")
            else:
                circle = Circle(Point(160, 440), 45)
                circle.setWidth(2)
                if (plays[6] == ' '):
                    circle.draw(board)
                    plays[6] = 'O'
                    labelT.setText("Your turn Player 1")
        elif (click.getX() > 220 and click.getX() < 380 and click.getY() > 100 and click.getY() < 220):
            if (i % 2 == 0):
                line1 = Line(Point(240, 120), Point(360, 200))
                line1.setWidth(2)
                line1.draw(board)
                line2 = Line(Point(360, 120), Point(240, 200))
                line2.setWidth(2)
                line2.draw(board)
                plays[1] = 'X'
                labelT.setText("Your turn Player 2")
            else:
                circle = Circle(Point(300, 160), 45)
                circle.setWidth(2)
                if (plays[1] == ' '):
                    circle.draw(board)
                    plays[1] = 'O'
                    labelT.setText("Your turn Player 1")
        elif (click.getX() > 220 and click.getX() < 380 and click.getY() > 220 and click.getY() < 380):
            if (i % 2 == 0):
                line1 = Line(Point(240, 240), Point(360, 360))
                line1.setWidth(2)
                line1.draw(board)
                line2 = Line(Point(360, 240), Point(240, 360))
                line2.setWidth(2)
                line2.draw(board)
                plays[4] = 'X'
                labelT.setText("Your turn Player 2")
            else:
                circle = Circle(Point(300, 300), 45)
                circle.setWidth(2)
                if (plays[4] == ' '):
                    circle.draw(board)
                    plays[4] = 'O'
                    labelT.setText("Your turn Player 1")
        elif (click.getX() > 220 and click.getX() < 380 and click.getY() > 380 and click.getY() < 500):
            if (i % 2 == 0):
                line1 = Line(Point(240, 400), Point(360, 480))
                line1.setWidth(2)
                line1.draw(board)
                line2 = Line(Point(360, 400), Point(240, 480))
                line2.setWidth(2)
                line2.draw(board)
                plays[7] = 'X'
                labelT.setText("Your turn Player 2")
            else:
                circle = Circle(Point(300, 440), 45)
                circle.setWidth(2)
                if (plays[7] == ' '):
                    circle.draw(board)
                    plays[7] = 'O'
                    labelT.setText("Your turn Player 1")
        elif (click.getX() > 380 and click.getX() < 500 and click.getY() > 100 and click.getY() < 220):
            if (i % 2 == 0):
                line1 = Line(Point(400, 120), Point(480, 200))
                line1.setWidth(2)
                line1.draw(board)
                line2 = Line(Point(480, 120), Point(400, 200))
                line2.setWidth(2)
                line2.draw(board)
                plays[2] = 'X'
                labelT.setText("Your turn Player 2")
            else:
                circle = Circle(Point(440, 160), 45)
                circle.setWidth(2)
                if (plays[2] == ' '):
                    circle.draw(board)
                    plays[2] = 'O'
                    labelT.setText("Your turn Player 1")
        elif (click.getX() > 380 and click.getX() < 500 and click.getY() > 220 and click.getY() < 380):
            if (i % 2 == 0):
                line1 = Line(Point(400, 240), Point(480, 360))
                line1.setWidth(2)
                line1.draw(board)
                line2 = Line(Point(480, 240), Point(400, 360))
                line2.setWidth(2)
                line2.draw(board)
                plays[5] = 'X'
                labelT.setText("Your turn Player 2")
            else:
                circle = Circle(Point(440, 300), 45)
                circle.setWidth(2)
                if (plays[5] == ' '):
                    circle.draw(board)
                    plays[5] = 'O'
                    labelT.setText("Your turn Player 1")
        elif (click.getX() > 380 and click.getX() < 500 and click.getY() > 380 and click.getY() < 500):
            if (i % 2 == 0):
                line1 = Line(Point(400, 400), Point(480, 480))
                line1.setWidth(2)
                line1.draw(board)
                line2 = Line(Point(480, 400), Point(400, 480))
                line2.setWidth(2)
                line2.draw(board)
                plays[8] = 'X'
                labelT.setText("Your turn Player 2")
            else:
                circle = Circle(Point(440, 440), 45)
                circle.setWidth(2)
                if (plays[8] == ' '):
                    circle.draw(board)
                    plays[8] = 'O'
                    labelT.setText("Your turn Player 1")
                    
        res = check(plays, board)
        if (res == "X"):
            labelT.setText("Player 1 won!")
            labelB.setText("Click to close")
            click2 = board.getMouse()
            if (click2.getX() > 100 and click2.getX() < 500 and click2.getY() > 500 and click2.getY() < 600):
                flag = 0
                board.close()
        elif (res == "O"):
            labelT.setText("Player 2 won!")
            labelB.setText("Click to close")
            click2 = board.getMouse()
            if (click2.getX() > 100 and click2.getX() < 500 and click2.getY() > 500 and click2.getY() < 600):
                flag = 0
                board.close()
        else:
            continue

    if (flag != 0):
        labelT.setText("It's a tie...")
        labelB.setText("Click to close")
        click = board.getMouse()
        if (click.getX() > 100 and click.getX() < 500 and click.getY() > 500 and click.getY() < 600):
            board.close()
            
    return board, labelT, labelB, numPlayers

#define the check function which checks for any winning patterns
def check(grid, board):
    if (grid[0] == "X" and grid[1] == "X" and grid[2] == "X"):
        win = Line(Point(100, 160), Point(500, 160))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "X"
    elif (grid[0] == "O" and grid[1] == "O" and grid[2] == "O"):
        win = Line(Point(100, 160), Point(500, 160))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "O"
    elif (grid[0] == "X" and grid[3] == "X" and grid[6] == "X"):
        win = Line(Point(160, 100), Point(160, 500))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "X"
    elif (grid[0] == "O" and grid[3] == "O" and grid[6] == "O"):
        win = Line(Point(160, 100), Point(160, 500))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "O"
    elif (grid[0] == "X" and grid[4] == "X" and grid[8] == "X"):
        win = Line(Point(120, 120), Point(480, 480))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "X"
    elif (grid[0] == "O" and grid[4] == "O" and grid[8] == "O"):
        win = Line(Point(120, 120), Point(480, 480))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "O"
    elif (grid[1] == "X" and grid[4] == "X" and grid[7] == "X"):
        win = Line(Point(300, 120), Point(300, 480))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "X"
    elif (grid[1] == "O" and grid[4] == "O" and grid[7] == "O"):
        win = Line(Point(300, 120), Point(300, 480))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "O"
    elif (grid[2] == "X" and grid[5] == "X" and grid[8] == "X"):
        win = Line(Point(440, 120), Point(440, 480))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "X"
    elif (grid[2] == "O" and grid[5] == "O" and grid[8] == "O"):
        win = Line(Point(440, 120), Point(440, 480))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "O"
    elif (grid[3] == "X" and grid[4] == "X" and grid[5] == "X"):
        win = Line(Point(100, 300), Point(500, 300))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "X"
    elif (grid[3] == "O" and grid[4] == "O" and grid[5] == "O"):
        win = Line(Point(100, 300), Point(500, 300))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "O"
    elif (grid[6] == "X" and grid[7] == "X" and grid[8] == "X"):
        win = Line(Point(100, 440), Point(500, 440))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "X"
    elif (grid[6] == "O" and grid[7] == "O" and grid[8] == "O"):
        win = Line(Point(100, 440), Point(500, 440))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "O"
    elif (grid[2] == "X" and grid[4] == "X" and grid[6] == "X"):
        win = Line(Point(480, 120), Point(120, 480))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "X"
    elif (grid[2] == "O" and grid[4] == "O" and grid[6] == "O"):
        win = Line(Point(480, 120), Point(120, 480))
        win.setWidth(4)
        win.setFill("red")
        win.draw(board)
        return "O"
    else:
        return "FALSE"

#The main function which starts the program and detects any clicks in the control panel
def main():
    controlWin, onePlayer, twoPlayer, exitB = create()
    winExistence = False
    global win
    global labelT
    global labelB
    global numPlayers
    count = 0
    while True:
        click = controlWin.getMouse()
        if (click.getX() > 115 and click.getX() < 265 and click.getY() > 300 and click.getY() < 350):
            break;
        elif (click.getX() > 50 and click.getX() < 180 and click.getY() > 200 and click.getY() < 250):
            # 1 Player Game
            if (winExistence == True):
                win.close()
            winExistence = True
            win, labelT, labelB, numPlayers = board(1)
        elif (click.getX() > 200 and click.getX() < 330 and click.getY() > 200 and click.getY() < 250):
            # 2 player game
            if (winExistence == True):
                win.close()
            winExistence = True
            win, labelT, labelB, numPlayers = board(2)
        else:
            continue
    if (winExistence == True):
        win.close()
    controlWin.close()

main()
