import curses
import helpers
import windows


class Interface:
    def __init__(self, taskWin, pageMenu, n):
        self.tasks = helpers.getTasks()
        self.taskWin = taskWin
        self.movementWindow = windows.getMovementWindow()
        self.pageMenu = pageMenu
        self.cursorLimit = curses.LINES - 7
        self.lines = curses.LINES - 5
        self.cols = curses.COLS - 4
        self.n = n
        self.y = 0
        self.cursor = 0
        self.cursorPos = 0
        self.task = 0
        self.page = 1
        self.acceptedMoves = {
                "KEY_UP": self.keyUp,
                "KEY_DOWN": self.keyDown,
                "f": self.keyF,
                "r": self.keyR,
                "q": self.keyQ
                }


    def keyListener(self):

        while True:
            key = self.movementWindow.getkey()

            if key in self.acceptedMoves:
                function = self.acceptedMoves[key]
                function()

    
    def scrollUp(self):
        self.y -= self.lines
        self.cursor = self.cursorLimit
        self.cursorPos -= 2
        self.task -= 1
        self.page -= 1


    def scrollDown(self):
        self.cursor = 0
        self.cursorPos += 2
        self.y += self.lines   # Scroll one screen down
        self.page += 1
        self.task += 1


    def keyUp(self):
        if self.cursor == 0 and self.y > 0:
            self.scrollUp()
            helpers.updatePageNumber(self.pageMenu, self.page)
            self.taskWin.refresh(self.y, 0, 1, 6, self.lines, self.cols)

        elif self.cursor > 0:
            self.cursor -= 2
            self.task -= 1
            self.cursorPos -= 2

        helpers.updateMovementWin(self.movementWindow, self.cursor)


    def keyDown(self):
        if self.cursorPos < self.n - 2:

            if self.cursor + 2 > self.cursorLimit:
                self.scrollDown()
                helpers.updatePageNumber(self.pageMenu, self.page)
                self.taskWin.refresh(self.y, 0, 1, 6, self.lines, self.cols)

            else:
                self.cursor += 2
                self.cursorPos += 2
                self.task += 1

            helpers.updateMovementWin(self.movementWindow, self.cursor)
                
    
    # Opening csv too many times, need to store it as an attribute
    # for better design
    def keyF(self):
        helpers.finishTask(self.task, self.tasks)
        self.taskWin.refresh(self.y, 0, 1, 6, self.lines, self.cols)
        helpers.updateTasks(helpers.getTasks(), self.taskWin, self.y)


    def keyR(self):
        helpers.removeTask(self.task, self.tasks)

        self.cursor -= 2

        # Cursor on top, not on first task
        if self.cursor < 0 and self.task > 0:
            self.decreaseValues()
            self.cursor = self.cursorLimit
            self.y -= self.lines    # Scroll one page up
            self.page -= 1

        # Cursor on top, first task
        elif self.cursor < 0 and self.task == 0:
            self.cursor = 0
            self.n -= 2

        else:
            self.decreaseValues()

        # Refresh tasks, page number and cursor position
        self.refreshAll()


    def keyQ(self):
        exit(0)


    def decreaseValues(self):
        self.cursorPos -= 2
        self.task -= 1
        self.n -= 2


    # Refreshes task window, page number and cursor position
    def refreshAll(self):
        self.taskWin.refresh(self.y, 0, 1, 6, self.lines, self.cols)
        helpers.updatePageNumber(self.pageMenu, self.page)
        helpers.updateTasks(helpers.getTasks(), self.taskWin, self.y)
        helpers.updateMovementWin(self.movementWindow, self.cursor)
