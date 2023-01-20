# todoTUI (under development)

## About

todoTUI is a minimalistic to-do list app written in Python and relies on `curses`. 
The movement is based on keyboard, where the user can add, finish and remove tasks. 
The user can also scroll through different pages of tasks (in case there are more tasks that the terminal can display).

## Pre-usage (not working yet)

```
python3 setup.py install
```

## Usage

> #### Flags
>
> - h (--help) Help menu
> - a Add tasks
> - l List tasks

#### Opening app
```
todo
```

#### Using flags
 
###### Add tasks

```
todo -a "Your task goes here"
```

###### Open help menu

```
todo --help
```

###### List tasks

```
todo -l
```

> #### Movement and task management
>
> - Arrow Up: Scroll up
> - Arrow Down: Scroll down
> - f: Finish task
> - r: Remove task
