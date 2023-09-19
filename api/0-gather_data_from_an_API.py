#!/usr/bin/python3
""" This module defines the REST API """
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()

    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo["completed"])

    print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), completed_tasks, total_tasks))

    [print(f"\t {todo['title']}") for todo in todos if todo["completed"]]
