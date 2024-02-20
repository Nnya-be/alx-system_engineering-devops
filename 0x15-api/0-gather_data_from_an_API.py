#!/usr/bin/python3
"""A script to get information about a person to do lists."""
import requests
from sys import argv


if __name__ == '__main__':
    todos = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    user = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    tsk = requests.get(todos).json()
    uses = requests.get(user).json()
    tsk_t = [task['title'] for task in tsk if task.get('completed')]
    m = f"Employee {uses['name']} is done with tasks ({len(tsk_t)}/{len(tsk)}:"
    print(m)
    for title in tsk_t:
        print(f'\t{title}')
