#!/usr/bin/python3
import requests
from sys import argv

"""A script to get information about a person to do lists."""

if __name__ == '__main__':
    todos = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    user = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    tasks = requests.get(todos).json()
    users = requests.get(user).json()
    task_title = [task['title'] for task in tasks if task.get('completed')]
    print(f"Employee {users['name']} is done with tasks ({len(task_title)}/{len(tasks)}:")
    for title in task_title:
        print(f'\t{title}')
