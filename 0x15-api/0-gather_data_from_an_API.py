#!/usr/bin/python3
import requests
import sys

"""A script to get information about a person to do lists."""

if __name__ == '__main__':
    api_url = f'https://jsonplaceholder.typicode.com/todos/{sys.argv[1]}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        todos = response.json()

        employee_name = todos[0]['username']
        total_tasks = len(todos)
        completed_tasks = sum(todo['completed'] for todo in todos)

        print(f'Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):')
        print(f'\t{employee_name}: {completed_tasks}/{total_tasks}')

    except requests.RequestException:
        print(f'An error occured while fetching the data')
