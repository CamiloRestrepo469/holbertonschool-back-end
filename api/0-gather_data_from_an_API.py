#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        if user_response.status_code != 200 or todos_response.status_code != 200:
            print("Error: No se pudo acceder a la información del empleado o de las tareas.")
            return

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data["name"]
        total_tasks = len(todos_data)
        done_tasks = sum(1 for task in todos_data if task["completed"])
        
        print(f"Empleado {employee_name} ha completado tareas ({done_tasks}/{total_tasks}):")
        for task in todos_data:
            if task["completed"]:
                print(f"    {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        get_employee_todo_progress(employee_id)
