import curses
from curses import wrapper
import helpers
from geometry import createRectangle, getTaskRectangle, getMenuRectangle


# Checking arguments passed on execution
helpers.checkArgs()

# Initializing curses
stdscr = curses.initscr()


# Needs refactoring
def main(stdscr):
    stdscr.clear()
    
    #createRectangle(stdscr)
    getTaskRectangle(stdscr)
    getMenuRectangle(stdscr)
    stdscr.refresh()
    n, taskWin = helpers.showTasks()
    helpers.move(n, taskWin)


wrapper(main)
