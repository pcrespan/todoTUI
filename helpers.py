import argparse
import csv


parser = argparse.ArgumentParser(prog="todoTUI", description="TUI to-do list")
parser.add_argument("-a", help="Add task")
args = parser.parse_args()


def addTask(task, description):
    with open("todoTasks.csv") as file:
        writer = csv.DictWriter(file, fieldnames=["task", "description"])
        writer.writerow({"task": task, "description": description})
