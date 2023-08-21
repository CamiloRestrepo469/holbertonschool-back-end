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
        EMPLOYEE_NAME) > 17 else EMPLOYEE_NAME
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = sum(1 for task in data if task["completed"])
    TASK_TITLE = [task["title"] for task in data if task["completed"]]

    # Print Employee Name: OK/Incorrect
    print(
        f"Employee Name: {'OK' if len(EMPLOYEE_NAME) == 17 else 'Incorrect'}")

    # Print To Do Count: OK/Incorrect
    print(
        f"To Do Count: {'OK' if TOTAL_NUMBER_OF_TASKS == len(data) else 'Incorrect'}")

    # Print First line formatting: OK/Incorrect
    print(
        f"First line formatting: {'OK' if len(EMPLOYEE_NAME) == 17 and TOTAL_NUMBER_OF_TASKS == len(data) else 'Incorrect'}")

    # Print Task 1 to Task N Formatting: OK/Not in output
    for i, title in enumerate(TASK_TITLE, start=1):
        print(
            f"Task {i} {'Formatting: OK' if title in TASK_TITLE else 'not in output'}")
