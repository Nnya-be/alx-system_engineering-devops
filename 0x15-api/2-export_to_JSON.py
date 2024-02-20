#!/usr/bin/python3
"""Retrieve user and corresponding done tasks, export data in JSON format."""
import requests
from sys import argv
import json


if __name__ == '__main__':
    userId = argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{userId}"
    task_url = f"https://jsonplaceholder.typicode.com/todos?userId={userId}"

    user = requests.get(user_url).json()
    tsks = requests.get(task_url).json()

    json_data = {
        userId: [
            {"task": task['title'],
             "completed": task['completed'],
             "username": user['username']} for task in tsks
        ]
    }


    json_file_path = f"{userId}.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

    print(f"JSON file '{json_file_path}' created successfully.")
