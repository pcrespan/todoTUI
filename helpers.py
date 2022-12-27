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
        print("juao")

        for task, description in reader:
            tasks.append({"task": task, "description": description})
    return tasks


def checkArgs():
    parser = argparse.ArgumentParser(prog="todoTUI", description="TUI to-do list")
    parser.add_argument("-a", nargs=2, help="Add task")
    args = parser.parse_args()

    if args.a:
        addTask(args.a[0], args.a[1])
        print("Task successfully added")
