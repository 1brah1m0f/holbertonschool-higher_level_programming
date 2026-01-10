#!/usr/bin/python3
"""Docstring for restful-api.task_02_requests"""

import json
import requests
import csv

response = requests.get('https://jsonplaceholder.typicode.com/posts')


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        data = response.json()
        for i in data:
            print(i['title'])


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()
    with open(data, "w",encoding="utf-8") as f:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for post in data:
            writer.writerow({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
