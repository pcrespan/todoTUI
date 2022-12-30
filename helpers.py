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
    taskWinPosy = 0
    cursor = 0
    
    movementWindow = curses.newpad(n * 2, 3)
    movementWindow.keypad(True)
    movementWindow.clear()
    moveCursor(cursor, y, movementWindow)
    movementWindow.refresh(0, 0, 1, 3, curses.LINES - 2, 3)

    while True:
        key = movementWindow.getkey()
        
        if key == "KEY_UP" and y > 0:
            y -= 1
            cursor -= 1
            taskWinPosy -= 1
            taskWin.refresh(taskWinPosy, 0, 2, 6, curses.LINES - 2, curses.COLS - 4)
        elif key == "KEY_DOWN" and y < n * 2:
            y += 1
            cursor += 1
            taskWinPosy += 1
            taskWin.refresh(taskWinPosy, 0, 2, 6, curses.LINES - 2, curses.COLS - 4)
        elif key == 'q':
            exit(0)
        moveCursor(cursor, y, movementWindow)


def moveCursor(cursor, y, window):
    if y < 0 or cursor < 0:
        y = 0
        cursor = 0
    if cursor > curses.LINES - 5:
        cursor = curses.LINES - 5
    window.clear()
    window.addstr(y, 2, "x")
    window.refresh(0, 0, 1, 3, curses.LINES - 2, 3)
