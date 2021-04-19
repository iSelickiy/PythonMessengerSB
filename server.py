from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world!'


@app.route('/status')
def status_json():
    return jsonify(
        status=True,
        name='My First Messenger',
        time=datetime.now()
    )


app.run()
