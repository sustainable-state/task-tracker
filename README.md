# Task Tracker

A simple command-line task tracker written in Python.

The application allows you to add, update, delete, and manage tasks from the command line.

## Features

* Add a new task
* Update a task
* Delete a task
* Mark a task as in progress
* Mark a task as done
* List all tasks
* List tasks by status
* Store tasks in a JSON file

## Requirements

* Python 3
* No external libraries are required

## Installation

Clone the repository and go to the project directory:

```bash
git clone <repository-url>
cd task-tracker
```

## Usage

### Add a task

```bash
python task_cli.py add "Buy groceries"
```

### Update a task

```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### Delete a task

```bash
python task_cli.py delete 1
```

### Mark a task as in progress

```bash
python task_cli.py mark-in-progress 1
```

### Mark a task as done

```bash
python task_cli.py mark-done 1
```

### List all tasks

```bash
python task_cli.py list
```

### List completed tasks

```bash
python task_cli.py list done
```

### List tasks that are not done

```bash
python task_cli.py list todo
```

### List tasks in progress

```bash
python task_cli.py list in-progress
```

## Data Storage

Tasks are stored in a `tasks.json` file in the project directory.

Each task contains:

* `id` - unique task identifier
* `description` - task description
* `status` - task status
* `createdAt` - task creation date and time
* `updatedAt` - last update date and time

## Statuses

Tasks can have one of the following statuses:

* `todo`
* `in-progress`
* `done`
