#!/usr/bin/python3
"""A script to get information about a person to do lists."""
import requests
from sys import argv


if __name__ == '__main__':
    Id = argv[1]
    url_task = f"https://jsonplaceholder.typicode.com/todos?userId={Id}"
    url_user = f"https://jsonplaceholder.typicode.com/users/{Id}"
    user = requests.get(url_user).json()
    tasks = requests.get(url_task).json()

    # Use a list comprehension to create the task_titel list
    task_title = [task['title'] for task in tasks if task.get('completed')]
    done = f'is done with tasks'
    print(f"Employee {user['name']} {done} ({len(task_title)}/{len(tasks)}):")

    for title in task_title:
        print(f"\t{title}")
