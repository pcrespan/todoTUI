import curses
import argparse
import csv


def addTask(task):
    with open("todoTasks.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["task", "status"])
        writer.writerow({"task": task, "status": "todo"})


def getTasks():
    tasks = []

    with open("todoTasks.csv", "r") as file:
        reader = csv.DictReader(file)

        for task in reader:
            tasks.append(task)
    return tasks


def finishTask(taskNumber):
    tasks = getTasks()
    with open("todoTasks.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["task", "status"])
        tasks[taskNumber]["status"] = "finished"
        # Re-writing header and tasks to csv file
        writer.writeheader()
        writer.writerows(tasks)


def checkArgs():
    parser = argparse.ArgumentParser(prog="todoTUI", description="TUI to-do list")
    parser.add_argument("-a", help="Add task")
    parser.add_argument("-f", help="Finish task")
    args = parser.parse_args()

    if args.a:
        addTask(args.a)
        print("Task successfully added")
        exit(0)

    if args.f:
        taskNumber = int(args.f) - 1
        finishTask(taskNumber)
        print(f"Task finished.")
        exit(0)


def move(n, taskWin):
    y = 0
    
    movementWindow = curses.newwin(curses.LINES - 3, 3, 2, 2)
    movementWindow.keypad(True)
    movementWindow.clear()
    movementWindow.refresh()

    while True:
        key = movementWindow.getkey()
        if key == "KEY_UP" and y > 0:
            y -= 2
            taskWin.refresh(y, 0, 2, 6, curses.LINES - 2, curses.COLS - 4)
        # y < n + 2 - curses.LINES to avoid scrolling past one whole screen
        # + 2 because of window size (beginning and end)
        elif key == "KEY_DOWN" and y < n + 2 - curses.LINES:
            y += 2
            taskWin.refresh(y, 0, 2, 6, curses.LINES - 2, curses.COLS - 4)
        elif key == 'q':
            exit(0)
