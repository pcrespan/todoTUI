import argparse
import csv


def addTask(task, description):
    with open("todoTasks.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["task", "description"])
        writer.writerow({"task": task, "description": description})


parser = argparse.ArgumentParser(prog="todoTUI", description="TUI to-do list")
parser.add_argument("-a", nargs="+", help="Add task")
args = parser.parse_args()

if args.a:
    addTask(args.a[0], args.a[1])
