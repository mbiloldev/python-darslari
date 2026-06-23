from graphics import GraphWin, Rectangle, Point
from itertools import cycle

def main():
    print (("Please enter four comma seperated colours e.g.:"
             "'red,green,blue'\n" 
             "Allowed colours are: red, green, blue, yellow and cyan"))
    colours = input("Enter your four colours: ").split(',')
    print ("Please enter gridsize e.g.: '100'")
    gsize = int(input("Enter gridsize: "))
    win_size = 250
    win = GraphWin("Squares", win_size, win_size)
    drawSquares(win, gsize, win_size, colours)
    win.getMouse()
    win.close()

def drawSquares(win, gsize, winsize, colours):
    side = winsize / gsize
    color = cycle(colours)
    for row in range(gsize):
        y1 = row * side
        y2 = y1 + side
        for column in range(gsize):
            x1 = column * side
            x2 = x1 + side
            rect = Rectangle(Point(x1, y1), Point(x2, y2))
            rect.setFill(color.next())
            rect.draw(win)

main()
