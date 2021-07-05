import numpy as np
import time
from graphics import *


def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

hw = int(input("Window Size:"))
xysize = int(input("Board Size:"))
OnColor = str(input("On Color:"))
OffColor = str(input("Off Color:"))

startBoard = np.random.randint(0, 2, size=(xysize, xysize))
nextStep = np.full(startBoard.shape, 0)

#print(startBoard)
wHeight = hw
wWidth = hw

window = GraphWin(width = wWidth, height = wHeight, autoflush=False)

squareOrigin = Point(0, 0)
increaseAmountX = 0
newSquareHeight = 0


for i in range(50):
    #time.sleep(1)
    #clear(window)
    squareOrigin.y = 0
    for r in range(xysize):
        for c in range(xysize):
            iNei = 0
                #cardinal directions
                #check left & right
            try:
                if startBoard[r+1][c] == 1:
                    iNei += 1
            except:
                iNei += 0
            try:
                if startBoard[r-1][c] == 1:
                    iNei += 1
            except:
                iNei += 0
                #check up & down
            try:
                if startBoard[r][c+1] == 1:
                    iNei += 1
            except:
                iNei += 0
            try:
                if startBoard[r][c-1] == 1:
                    iNei += 1
            except:
                iNei += 0

                #diagonals
            try:
                if startBoard[r+1][c+1] == 1:
                    iNei += 1
            except:
                iNei += 0
            try:
                if startBoard[r-1][c-1] == 1:
                    iNei += 1
            except:
                iNei += 0
            try:
                if startBoard[r+1][c-1] == 1:
                    iNei += 1
            except:
                iNei += 0
            try:
                if startBoard[r-1][c+1] == 1:
                    iNei += 1
            except:
                iNei += 0

            if startBoard[r][c] == 1 and iNei < 2:
               nextStep[r][c] = 0
            elif startBoard[r][c] == 1 and iNei > 3:
               nextStep[r][c] = 0
            elif startBoard[r][c] == 0 and iNei == 3:
                nextStep[r][c] = 1
            else:
               nextStep[r][c] = startBoard[r][c]

            squareOrigin.x += increaseAmountX
            newSquare = Rectangle(squareOrigin, Point(squareOrigin.x + wWidth/xysize, squareOrigin.y + wHeight/xysize))
            if startBoard[r][c] == 1:
                newSquare.setFill(OnColor)
            else:
                newSquare.setFill(OffColor)

            if squareOrigin.x < wWidth:
                increaseAmountX = wWidth/xysize
            elif squareOrigin.x >= wWidth:
                increaseAmountX = 0
                squareOrigin.x = 0
                squareOrigin.y += wHeight/xysize

            addedObj = newSquare

            addedObj.draw(window)
            update(60)

    #print("\n", "-" * 25, "\n")
    #print(nextStep)
    startBoard = nextStep
    #nextStep = np.full(startBoard.shape, 0)