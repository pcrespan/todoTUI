import curses
import argparse
import csv
import windows


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
    updatedStatus = ""

    with open("todoTasks.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["task", "status"])

        if tasks[taskNumber]["status"] == "finished":
            tasks[taskNumber]["status"] = "todo"
            updatedStatus = "restored"
        else:
            tasks[taskNumber]["status"] = "finished"
            updatedStatus = "finished"

        # Re-writing header and tasks to csv file
        writer.writeheader()
        writer.writerows(tasks)

        return updatedStatus


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
        status = finishTask(taskNumber)
        print(f"Task {status}.")
        exit(0)


# Needs refactoring
def showTasks():
    tasks = getTasks()
    taskQtd = len(tasks) * 2

    taskWin = windows.getTaskWin(taskQtd)

    n = 0
    i = 1

    for task in tasks:
        if task["status"] == "finished":
            taskWin.addstr(n, 0, "" + " " + str(i) + "." + " " + task["task"])
        else:
            taskWin.addstr(n, 0, str(i) + "." + " " + task["task"])
        i += 1
        n += 2
    taskWin.refresh(0, 0, 2, 6, curses.LINES - 2, curses.COLS - 4)

    # n is where the last task is located
    return n, taskWin


def move(n, taskWin):
    y = 0
   
    movementWindow = windows.getMovementWindow()

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
