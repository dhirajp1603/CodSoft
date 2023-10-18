
#TASK 1 :- TO-DO LIST

"""A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line application using Python, allowing
users to create, update, and track their to-do lists"""

import json

# Task list
tasks = []

def save_tasks(filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_task(title, description, due_date):
    task = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)

def list_tasks():
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{idx}. {task['title']} ({task['due_date']}): {status}")

def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
    else:
        print("Invalid task index.")

def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Deleted task: {deleted_task['title']}")
    else:
        print("Invalid task index.")

def main():
    filename = 'tasks.json'
    tasks.extend(load_tasks(filename))
    while True:
        print("\nTo-Do List:")
        list_tasks()
        print("\nMenu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Save and Quit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date: ")
            add_task(title, description, due_date)
        elif choice == '2':
            task_index = int(input("Enter the task number to mark as completed: "))
            complete_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter the task number to delete: "))
            delete_task(task_index)
        elif choice == '4':
            save_tasks(filename)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select (1/2/3/4)")

if __name__ == "__main__":
    main()
