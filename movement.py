import curses
import helpers
import windows


def scrollUp(y, cursor, cursorPos, task, page):
    y -= curses.LINES - 5
    cursor = curses.LINES - 7
    cursorPos -= 2
    task -= 1
    page -= 1
    return y, cursor, cursorPos, task, page


def scrollDown(y, cursor, cursorPos, task, page):
    cursor = 0
    y += curses.LINES - 5   # Scroll one screen down
    page += 1
    task += 1
    return y, cursor, cursorPos, task, page


# Might be good to create scrollUp and scrollDown functions
def move(n, taskWin, pageMenu):
    # Setting initial values
    y, cursor, cursorPos, task, page = helpers.setInitialValues()

    lines = curses.LINES - 5
    cols = curses.COLS - 4

    movementWindow = windows.getMovementWindow()

    while True:
        key = movementWindow.getkey()

        # Obviously needs refactoring
        if key == "KEY_UP":

            if cursor == 0 and y > 0:
                y, cursor, cursorPos, task, page = scrollUp(y, cursor, cursorPos, task, page)
                helpers.updatePageNumber(pageMenu, page)
                taskWin.refresh(y, 0, 1, 6, lines, cols)

            elif cursor > 0:
                cursor -= 2
                task -= 1
                cursorPos -= 2
            helpers.updateMovementWin(movementWindow, cursor)

        elif key == "KEY_DOWN" and cursorPos < n - 2:
            cursor += 2
            cursorPos += 2

            if cursor > curses.LINES - 7:
                y, cursor, cursorPos, task, page = scrollDown(y, cursor, cursorPos, task, page)
                helpers.updatePageNumber(pageMenu, page)
                taskWin.refresh(y, 0, 1, 6, lines, cols)

            else:
                task += 1
            helpers.updateMovementWin(movementWindow, cursor)

        elif key == "f":
            # Needs refactoring. Opening csv file too many times
            helpers.finishTask(task)
            taskWin.refresh(y, 0, 1, 6, lines, cols)
            helpers.updateTasks(helpers.getTasks(), taskWin, y)

        elif key == "r":
            helpers.removeTask(task)
            # Avoiding extra scrolling
            cursor -= 2

            if cursor < 0 and task > 0:
                cursor = curses.LINES - 7
                task -= 1
                y -= lines
                cursorPos -= 2
                page -= 1
                n -= 2
                helpers.updatePageNumber(pageMenu, page)
                taskWin.refresh(y, 0, 1, 6, lines, cols)

            elif cursor < 0 and task == 0:
                cursor = 0
                n -= 2
                taskWin.refresh(y, 0, 1, 6, lines, cols)

            else:
                cursorPos -= 2
                task -= 1
                n -= 2
                taskWin.refresh(y, 0, 1, 6, lines, cols)
                helpers.updatePageNumber(pageMenu, page)
            helpers.updateTasks(helpers.getTasks(), taskWin, y)
            helpers.updateMovementWin(movementWindow, cursor)

        elif key == 'q':
            exit(0)

