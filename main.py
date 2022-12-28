import curses
from curses import wrapper
from curses.textpad import rectangle
import helpers


# Checking arguments passed on execution
helpers.checkArgs()

# Initializing curses
stdscr = curses.initscr()


# Needs refactoring
def main(stdscr):
    stdscr.clear()
    
    createRectangle()
    stdscr.refresh()
    n = showTasks()

    helpers.move(n)


# Needs refactoring
def showTasks():
    win = curses.newwin(curses.LINES - 4, curses.COLS - 8, 2, 6)
    tasks = helpers.getTasks()

    win.clear()
    win.refresh()

    n = 0

    for task in tasks:
        win.addstr(n, 2, task["task"])
        n += 2
    win.refresh()

    # n - 2 is where the last task is located
    return n - 2


def createRectangle():
    rectangle(stdscr, 1, 1, curses.LINES - 2, curses.COLS - 2)


wrapper(main)
