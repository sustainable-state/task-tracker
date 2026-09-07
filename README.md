# Task Tracker

A simple command-line task tracker written in Python.

## Features

* Add, update, and delete tasks
* Mark tasks as `in-progress` or `done`
* List all tasks or filter by status
* Store tasks in `tasks.json`

## Requirements

* Python 3
* No external libraries

## Usage

```bash
# Add a task
python task_cli.py add "Buy groceries"

# Update a task
python task_cli.py update 1 "Buy groceries and cook dinner"

# Delete a task
python task_cli.py delete 1

# Change status
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1

# List tasks
python task_cli.py list
python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress
```

## Data Storage

Tasks are stored in `tasks.json`.

Each task contains:

* `id`
* `description`
* `status`
* `createdAt`
* `updatedAt`

## Project

Based on the [Roadmap.sh Task Tracker project](https://roadmap.sh/projects/task-tracker).
