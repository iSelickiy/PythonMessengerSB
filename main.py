import time
from datetime import datetime


db = [{'name': None, 'text': None, 'time': None}]


def print_messages(messages):
    for message in messages:
        time_str = datetime.fromtimestamp(message['time'])
        print(message['name'], time_str)
        print(message['text'])
        print()

def send_message(name, text):
    db.append({'name': name, 'text': text, 'time': time.time()})

def get_messages(after):
    messages = [i for i in db if i['time'] > after]
    return messages [:50]

