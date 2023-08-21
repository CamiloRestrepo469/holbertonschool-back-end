#!/usr/bin/python3
"""import"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"missing employee id as argument")
        sys.exit(1)

    URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    EMPLOYEE_TODOS = requests.get(f"{URL}/users/{EMPLOYEE_ID}/todos",
                                  params={"_expand": "user"})
    data = EMPLOYEE_TODOS.json()

    EMPLOYEE_NAME = data[0]["user"]["name"]
    # Adjust the length of the employee name to match the expected format
    EMPLOYEE_NAME = EMPLOYEE_NAME[:17] if len(
        EMPLOYEE_NAME) > 18 else EMPLOYEE_NAME
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    for task in data:
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(task["title"])
    print(f"Employee Name: {EMPLOYEE_NAME} is done with tasks"
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for title in TASK_TITLE:
        print("\t ", title)
