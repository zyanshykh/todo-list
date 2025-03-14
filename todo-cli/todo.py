import click # to create cli
import json # to save and load tasks from a files
import os # to check if the file exists

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


@click.group()
def cli():
    """Simple Todo List manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task '{task}' added successfully.")


@click.command()
def list():
    """List all the tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{idx}. [{status}] {task['task']}")
        
        
@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed.")
    else:
        click.echo(f"Invalid task number: {task_number}")

@click.command()
@click.argument("task_number", type=int)
def delete(task_number):
    """Delete a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Deleted task: {deleted_task['task']}")
    else:
        click.echo(f"Invalid task number: {task_number}")



cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)
if __name__ == "__main__":
    cli()