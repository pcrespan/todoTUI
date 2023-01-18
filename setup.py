from setuptools import setup
from setuptools import find_packages


setup(
    name="todoTUI",
    version="1.0",
    description="TUI to-do list app",
    url="https://github.com/pcrespan/todoTUI",
    packages=find_packages('todo'),
    entry_points={
        "console_scripts": [
            'todo = todo.main:main'
        ],
    },
)
