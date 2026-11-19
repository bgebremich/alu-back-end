#!/usr/bin/python3
"""Exports the TODO lists of all employees to one JSON file."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        todos = requests.get(url + "todos",
                             params={"userId": user_id}).json()
        tasks = []
        for task in todos:
            tasks.append({"username": user.get("username"),
                          "task": task.get("title"),
                          "completed": task.get("completed")})
        all_tasks[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_tasks, f)
