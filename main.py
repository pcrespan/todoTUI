import curses
from curses import wrapper
from curses.textpad import rectangle
import helpers


# Checking arguments passed on execution
helpers.checkArgs()

# Initializing curses
stdscr = curses.initscr()


def main(stdscr):
    stdscr.clear()
    
    createRectangle()
    stdscr.refresh()
    mainPage()

    helpers.move()


def mainPage():
    win = curses.newwin(curses.LINES - 4, curses.COLS - 8, 2, 6)
    tasks = helpers.showTasks()

    win.clear()
    win.refresh()

    n = 0

    for task in tasks:
        win.addstr(n, 2, task["task"])
        n += 2
    win.refresh()


def createRectangle():
    rectangle(stdscr, 1, 1, curses.LINES - 2, curses.COLS - 2)


wrapper(main)
