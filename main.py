import curses
from curses import wrapper
import helpers
from geometry import getTaskRectangle, getMenuRectangle
import windows


# Checking arguments passed on execution
helpers.checkArgs()

# Checking if there are tasks
tasks = helpers.getTasks()

# Initializing curses
stdscr = curses.initscr()

# Needs refactoring
def main(stdscr):
    stdscr.clear()


    getTaskRectangle(stdscr)
    getMenuRectangle(stdscr)
    stdscr.refresh()

    n, taskWin = helpers.showTasks(tasks)
    windows.getMenuWin()
    pageMenu = windows.getPageMenu()
    helpers.move(n, taskWin, pageMenu)


wrapper(main)
