import curses
from curses import wrapper
from curses.textpad import rectangle
import helpers


helpers.checkArgs()
# Initializing curses
stdscr = curses.initscr()

def main(stdscr):
    stdscr.clear()
    
    mainPage(stdscr)
    createRectangle()

    stdscr.refresh()
    stdscr.getkey()


def mainPage(stdscr):
    tasks = helpers.showTasks()
    for task in tasks:
        stdscr.addstr(task["task"])


def createRectangle():
    rectangle(stdscr, 1, 1, curses.LINES - 2, curses.COLS - 2)

wrapper(main)
