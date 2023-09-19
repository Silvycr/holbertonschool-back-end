#!/usr/bin/python3
""" This module defines the REST API """
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()
    filename = "{}.csv".format(user["id"])

    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([user["id"], user["username"],
                            str(todo["completed"]), todo["title"]])
