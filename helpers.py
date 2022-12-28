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


def move(n):
    y = 0
    
    movementWindow = curses.newwin(curses.LINES - 4, 3, 2, 3)
    movementWindow.keypad(True)
    movementWindow.clear()
    moveCursor(y, movementWindow)
    movementWindow.refresh()

    while True:
        key = movementWindow.getkey()
        
        match key:
            case "KEY_UP":
                y -= 2
            case "KEY_DOWN":
                y += 2
            case "q":
                exit(0)
        if y < 0:
            y = 0
        elif y > n:
            y = n
        moveCursor(y, movementWindow)


def moveCursor(y, window):
    window.clear()
    window.addstr(y, 2, "x")
    window.refresh()
