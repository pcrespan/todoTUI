import curses


def getMovementWindow():
    movementWindow = curses.newwin(1, 3, 2, 2)
    movementWindow.keypad(True)
    movementWindow.clear()
    movementWindow.refresh()
    return movementWindow


def getTaskWin(taskQtd):
    taskWin = curses.newpad(taskQtd, curses.COLS - 4)
    taskWin.scrollok(True)
    taskWin.clear()
    taskWin.refresh(0, 0, 2, 6, curses.LINES - 6, curses.COLS - 4)
    return taskWin
