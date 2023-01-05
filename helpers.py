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

        if taskNumber < 0:
            print("Invalid task number.")
            exit(1)

        status = finishTask(taskNumber)
        print(f"Task {status}.")
        exit(0)


# Needs refactoring
def showTasks(tasks):
    taskFinishedColor = getFinishedTaskColor()

    # Making window bigger so that it
    # doesn't glitch showing unwanted tasks
    taskQtd = len(tasks) * 4

    taskWin = windows.getTaskWin(taskQtd)

    n = 0
    i = 1

    for task in tasks:
        if task["status"] == "finished":
            taskWin.addstr(n, 0, "" + " " + str(i) + "." + " " + task["task"], taskFinishedColor)
        else:
            taskWin.addstr(n, 0, " " * 2 + str(i) + "." + " " + task["task"])
        i += 1
        n += 2
    taskWin.refresh(0, 0, 2, 6, curses.LINES - 5, curses.COLS - 4)

    # n is where the last task is located
    return n, taskWin


def getFinishedTaskColor():
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    taskFinishedColor = curses.color_pair(1)
    return taskFinishedColor


# Might be good to create scrollUp and scrollDown functions
def move(n, taskWin, pageMenu):
    y = 0
    page = 1
   
    movementWindow = windows.getMovementWindow()

    while True:
        key = movementWindow.getkey()
        if key == "KEY_LEFT" and y > 0:
            y -= curses.LINES - 5   # Scroll one screen up
            page -= 1
            updatePageNumber(pageMenu, page)
            taskWin.refresh(y, 0, 2, 6, curses.LINES - 5, curses.COLS - 4)
        # On the last screen, scroll just enough so that the words appear
        elif key == "KEY_RIGHT" and y < n + 4 - curses.LINES:
            y += curses.LINES - 5   # Scroll one screen down
            page += 1
            updatePageNumber(pageMenu, page)
            taskWin.refresh(y, 0, 2, 6, curses.LINES - 5, curses.COLS - 4)
        elif key == 'q':
            exit(0)


def updatePageNumber(pageMenu, page):
    pageMenu.clear()
    pageMenu.addstr(0, 0, f"Page {page}")
    pageMenu.refresh()
