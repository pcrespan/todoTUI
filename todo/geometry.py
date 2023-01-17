import curses
from curses.textpad import rectangle


def getTaskRectangle(stdscr):
    rectangle(stdscr, 0, 1, curses.LINES - 4, curses.COLS - 2)
    stdscr.addstr(0, round((curses.COLS - 5) / 2), "todoTUI")


def getMenuRectangle(stdscr):
    rectangle(stdscr, curses.LINES - 3, 1, curses.LINES - 1, curses.COLS - 2)
