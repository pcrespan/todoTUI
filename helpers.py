import curses
import argparse
import csv


def addTask(task, description):
    with open("todoTasks.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["task", "description"])
        writer.writerow({"task": task, "description": description})


def getTasks():
    tasks = []

    with open("todoTasks.csv", "r") as file:
        reader = csv.DictReader(file)

        for task in reader:
            tasks.append(task)
    return tasks


def checkArgs():
    parser = argparse.ArgumentParser(prog="todoTUI", description="TUI to-do list")
    parser.add_argument("-a", nargs=2, help="Add task")
    args = parser.parse_args()

    if args.a:
        addTask(args.a[0], args.a[1])
        print("Task successfully added")
        exit(0)


def move(n, taskWin):
    y = 0
    cursor = 0
    
    movementWindow = curses.newwin(curses.LINES - 3, 3, 2, 2)
    movementWindow.keypad(True)
    movementWindow.clear()
    moveCursor(cursor, y, movementWindow)
    movementWindow.refresh()

    while True:
        key = movementWindow.getkey()
        if key == "KEY_UP" and y > 0:
            cursor -= 1
            if cursor >= curses.LINES - 5:
                y -= 1
                taskWin.refresh(y, 0, 2, 6, curses.LINES - 2, curses.COLS - 4)
            y -= 1
            taskWin.refresh(y, 0, 2, 6, curses.LINES - 2, curses.COLS - 4)
        # y < n + 3 - curses.LINES to avoid scrolling past one whole screen
        # + 3 because of window size (beginning and end)
        elif key == "KEY_DOWN" and y < n + 3 - curses.LINES:
            if cursor >= curses.LINES - 5:
                y += 1
                taskWin.refresh(y, 0, 2, 6, curses.LINES - 2, curses.COLS - 4)
            y += 1
            cursor += 1
            taskWin.refresh(y, 0, 2, 6, curses.LINES - 2, curses.COLS - 4)
        elif key == 'q':
            with open("test.txt", "w") as file:
                file.write(str(y))
            exit(0)
        moveCursor(cursor, y, movementWindow)


def moveCursor(cursor, y, window):
    if y < 0 or cursor < 0:
        y = 0
        cursor = 0
        return
    if cursor > curses.LINES - 5:
        cursor = curses.LINES - 5
    window.clear()
    window.addstr(cursor, 2, "*")
    window.refresh()
