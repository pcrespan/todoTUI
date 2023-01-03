import curses
from curses.textpad import rectangle


def createRectangle(stdscr):
    rectangle(stdscr, 0, 1, curses.LINES - 1, curses.COLS - 2)


def getTaskRectangle(stdscr):
    rectangle(stdscr, 0, 1, curses.LINES - 4, curses.COLS - 2)


def getMenuRectangle(stdscr):
    rectangle(stdscr, curses.LINES - 3, 1, curses.LINES - 1, curses.COLS - 2)

