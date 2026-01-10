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
    # 1. Sorğunu göndəririk
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if response.status_code == 200:
        data = response.json()
        
        # 2. DÜZƏLİŞ: Faylın adı dırnaq içində string kimi yazılmalıdır ('posts.csv')
        # newline='' parametri boş sətirlərin yaranmaması üçündür
        with open('posts.csv', 'w', encoding='utf-8', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for post in data:
                # Yalnız lazım olan sahələri seçib yazırıq
                writer.writerow({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })
