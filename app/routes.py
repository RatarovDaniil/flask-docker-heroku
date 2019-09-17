# -*- coding: utf-8 -*-
from flask import render_template, Response
from app import app 
import time

def get_message():
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

@app.route('/', methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def index(path=None):
    return render_template("index.html")

@app.route('/stream')
def stream():
    def eventStream():
        while True:
            yield 'data: {}\n\n'.format(get_message())
    return Response(eventStream(), mimetype="text/event-stream")