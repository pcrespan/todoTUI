import curses
import windows
import helpers
import movement
from curses import wrapper
from geometry import getTaskRectangle, getMenuRectangle


# Checking arguments passed on execution
helpers.checkArgs()

# Checking if there are tasks
tasks = helpers.getTasks()

# Initializing curses
stdscr = curses.initscr()

# Making cursor invisible
curses.curs_set(0)

# Needs refactoring
def main(stdscr):
    stdscr.clear()


    getTaskRectangle(stdscr)
    getMenuRectangle(stdscr)
    stdscr.refresh()

    n, taskWin = helpers.showTasks(tasks)
    windows.getMenuWin()
    pageMenu = windows.getPageMenu()

    interface = movement.Interface(taskWin, pageMenu, n)
    interface.keyListener()


wrapper(main)
