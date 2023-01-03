import curses
from curses import wrapper
import helpers
from geometry import getTaskRectangle, getMenuRectangle
import windows


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
    windows.getMenuWin()
    pageMenu = windows.getPageMenu()
    helpers.move(n, taskWin, pageMenu)


wrapper(main)
