import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

# Initializing curses
stdscr = curses.initscr()

def main(stdscr):
    stdscr.clear()

    # Creating text box
    box = createBox()
    createRectangle()

    stdscr.refresh()
    box.edit()
    stdscr.getkey()


def createBox():
    win = curses.newwin(curses.LINES - 2, curses.COLS - 2)
    box = Textbox(win)
    return box


def createRectangle():
    rectangle(stdscr, 2, 2, curses.LINES - 2, curses.COLS - 2)

wrapper(main)
