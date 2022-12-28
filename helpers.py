import curses
import argparse
import csv


def addTask(task, description):
    with open("todoTasks.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["task", "description"])
        writer.writerow({"task": task, "description": description})


def showTasks():
    tasks = []

    with open("todoTasks.csv", "r") as file:
        reader = csv.DictReader(file)
        print(reader)

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


def move():
    
    movementWindow = curses.newwin(curses.LINES - 4, 2, 2, 3)
    movementWindow.clear()
    movementWindow.refresh()

    y = 0
    while True:
        key = movementWindow.getkey()
        
        if key == "KEY_UP" and y != 0:
            y += 2
            moveCursor(y, movementWindow)
        elif key == "KEY_DOWN" and y != curses.LINES - 4:
            y -= 2
            moveCursor(y, movementWindow)
        elif key == "q":
            exit(0)


def moveCursor(y, window):
    window.addstr(y, 2, "x")
    window.refresh()
