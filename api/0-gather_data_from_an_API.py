#!/usr/bin/python3
""" This module defines the REST API """
import requests
from sys import argv

URL = 'https://jsonplaceholder.typicode.com'


def get_name(id):
    response = requests.get(f'{URL}/users/{id}')
    response.raise_for_status()
    user_data = response.json()
    return user_data.get('name')


def get_todos(id):
    response = requests.get(f'{URL}/todos', params={'userId': id})
    response.raise_for_status()
    return response.json()


def display_todo(id):
    try:
        employee_name = get_name(id)
        todos = get_todos(id)

        completed_tasks = [task for task in todos if task['completed']]
        completed_count = len(completed_tasks)
        total_tasks = len(todos)

        print(f"Employee {employee_name} is done "
              f"with tasks({completed_count}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t {task['title']}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(argv) < 2:
        exit(1)

    employee_id = int(argv[1])
    display_todo(employee_id)
