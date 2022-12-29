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
    n, taskWin = showTasks()

    helpers.move(n, taskWin)


# Needs refactoring
def showTasks():
    tasks = helpers.getTasks()
    taskQtd = len(tasks) * 2
    win = curses.newpad(taskQtd, curses.COLS - 4)
    win.scrollok(True)

    win.clear()
    win.refresh(0, 0, 6, 6, curses.LINES - 2, curses.COLS - 4)

    n = 0

    for task in tasks:
        win.addstr(n, 2, task["task"])
        n += 2
    win.refresh(0, 0, 2, 6, curses.LINES - 2, curses.COLS - 4)

    # n - 2 is where the last task is located
    return n - 4, win


def createRectangle():
    rectangle(stdscr, 0, 1, curses.LINES - 1, curses.COLS - 2)


wrapper(main)
