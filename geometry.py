import curses
from curses.textpad import rectangle


def createRectangle(stdscr):
    rectangle(stdscr, 0, 1, curses.LINES - 1, curses.COLS - 2)
