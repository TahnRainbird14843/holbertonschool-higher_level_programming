"""
this is documented
"""

import requests
import csv


def fetch_and_print_posts():
    """this function gets posts and prints the titles"""
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    code = posts.status_code
    print("Status Code: {}".format(code))
    if (code == 200):
        data = posts.json()
        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    """this function gets posts and saves them to a csv file"""
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')

    if (posts.status_code == 200):
        with open('posts.csv', 'w') as f:
            data = posts.json()
            list_data = [dict(post) for post in data]
            for dictionary in list_data:
                del dictionary['userId']
            fieldnames = list(list_data[0].keys())
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(list_data)
