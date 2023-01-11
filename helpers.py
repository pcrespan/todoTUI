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

    if len(tasks) == 0:
        print("There are no tasks registered. Add one using -a.")
        exit(0)

    return tasks


def listTasks():
    tasks = getTasks()

    if tasks is not None:
        i = 1
        for task in tasks:
            if task["status"] == "finished":
                print("" + " " + str(i) + "." + task["task"])
            else:
                print(" " * 2 + str(i) + "." + " " + task["task"])
            i += 1
        exit(0)
    print("No tasks registered.")
    exit(1)
    

def finishTask(taskNumber):
    tasks = getTasks()
    updatedStatus = ""

    if taskNumber > len(tasks) - 1:
        print("Task doesn't exist.")
        exit(1)

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


def removeTask(taskNumber):
    tasks = getTasks()

    if taskNumber < 0 or taskNumber > len(tasks) - 1:
        print("Invalid task number.")
        exit(1)

    with open("todoTasks.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["task", "status"])

        del tasks[taskNumber]

        writer.writeheader()
        writer.writerows(tasks)


def checkArgs():
    parser = argparse.ArgumentParser(prog="todoTUI", description="TUI to-do list")
    parser.add_argument("-a", help="Add task")
    parser.add_argument("-f", help="Finish task")
    parser.add_argument("-r", help="Remove task")
    parser.add_argument("-l", help="List tasks", action="store_true")   # Action store_true means default=False
    args = parser.parse_args()

    if args.a:
        addTask(args.a)
        print("Task successfully added")
        exit(0)

    if args.f:
        taskNumber = int(args.f) - 1

        # Need to add this conditional to finishTask
        if taskNumber < 0:
            print("Invalid task number.")
            exit(1)
        status = finishTask(taskNumber)
        print(f"Task {status}.")
        exit(0)

    if args.r:
        taskNumber = int(args.r) - 1
        removeTask(taskNumber)

    if args.l:
        listTasks()


def printTasks(taskWin, taskFinishedColor, tasks):
    n = 0
    i = 1

    for task in tasks:
        if task["status"] == "finished":
            taskWin.addstr(n, 0, "" + " " + str(i) + "." + " " + task["task"], taskFinishedColor)
        else:
            taskWin.addstr(n, 0, " " * 2 + str(i) + "." + " " + task["task"])
        i += 1
        n += 2

    # This is probably unnecessary
    # n is where the last task is located
    return n


# Needs refactoring
def showTasks(tasks, taskWin):
    taskFinishedColor = getFinishedTaskColor()
    n = printTasks(taskWin, taskFinishedColor, tasks)
    # First refresh on screen
    taskWin.refresh(0, 0, 1, 6, curses.LINES - 5, curses.COLS - 4)
    return n


# Obviously needs refactoring
def updateTasks(tasks, taskWin, y):
    taskWin.clear()
    taskFinishedColor = getFinishedTaskColor()
    printTasks(taskWin, taskFinishedColor, tasks)
    # Refresh screen and show previous position
    taskWin.refresh(y, 0, 1, 6, curses.LINES - 5, curses.COLS - 4)


def getFinishedTaskColor():
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    taskFinishedColor = curses.color_pair(1)
    return taskFinishedColor


def setInitialValues():
    y = 0
    cursor = 0
    cursorPos = 0
    task = 0
    page = 1
    return y, cursor, cursorPos, task, page
    

def updateMovementWin(movementWindow, cursor):
    movementWindow.clear()
    movementWindow.addstr(cursor, 2, "")
    movementWindow.refresh()


def updatePageNumber(pageMenu, page):
    pageMenu.clear()
    pageMenu.addstr(0, 0, f"Page {page}")
    pageMenu.refresh()
