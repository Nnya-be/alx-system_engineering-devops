#!/usr/bin/python3
"""Retrieve tasks for all employees, export data in JSON format."""

import requests
import json

def fetch_user_tasks(user_id):
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}").json()
    tasks = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}").json()
    return {"username": user['username'], "tasks": [{"task": task['title'], "completed": task['completed']} for task in tasks]}

def export_all_employees_data():
    all_employees_data = {}
    for user_id in range(1, 11):  # Assuming user IDs are from 1 to 10
        all_employees_data[user_id] = fetch_user_tasks(user_id)
    
    # Write to JSON file
    json_file_path = "todo_all_employees.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(all_employees_data, json_file, indent=2)

    print(f"JSON file '{json_file_path}' created successfully.")

if __name__ == '__main__':
    export_all_employees_data()
