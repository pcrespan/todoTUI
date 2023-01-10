import curses


def getMovementWindow():
    movementWindow = curses.newwin(curses.LINES - 5, 3, 1, 2)
    movementWindow.keypad(True)
    movementWindow.clear()
    movementWindow.addstr(0, 2, "")
    movementWindow.refresh()
    return movementWindow


def getTaskWin(taskQtd):
    taskWin = curses.newpad(taskQtd, curses.COLS - 4)
    taskWin.scrollok(True)
    taskWin.clear()
    taskWin.refresh(0, 0, 1, 6, curses.LINES - 6, curses.COLS - 4)
    return taskWin


def getMenuWin():
    menuWin = curses.newwin(1, curses.COLS - 4, curses.LINES - 2, 2)
    menuWin.clear()
    menuWin.refresh()
    menuWin.addstr(0, 1, "  Up")
    menuWin.addstr(0, 8, " Down")
    menuWin.addstr(0, 16, "f Finish")
    menuWin.addstr(0, 26, "r Remove")
    menuWin.refresh()
    return menuWin


def getPageMenu():
    pageMenu = curses.newwin(1, 8, curses.LINES - 2, curses.COLS - 11)
    pageMenu.clear()
    pageMenu.addstr(0, 0, "Page 1")
    pageMenu.refresh()
    return pageMenu
