from flask import Flask, request, abort
from datetime import datetime
import time

app = Flask(__name__)
db = [
    {
        'name': 'Test',
        'text': 'Test',
        'time': 0.1
    },
    {
        'name': 'Test2',
        'text': 'Test2',
        'time': 0.2
    },
]


@app.route('/')
def hello():
    return 'Hello, world!'


@app.route('/status')
def status():
    return {
        'status': True,
        'name': 'My First messenger',
        'time': datetime.now()
    }

@app.route('/send', methods=['POST'])
def send_message():
    
    data = request.json

    if not isinstance(data, dict):
        return abort(400)


    if 'name' not in data and 'text' not in data:
        return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)
    if name == '' or text == '':
        return abort(400)

    db.append({'name': name, 'text': text, 'time': time.time()})
    return {'ok': True}

@app.route('/messages')
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    
    messages = [msg for msg in db if msg['time'] > after]
    return {'messages': messages[:50]}

app.run()
