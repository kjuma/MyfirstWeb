#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask


app= Flask(__name__)

@app.route('/')

def index():
    return "i am in capital of Rwanda"

@app.route('/<rda>')

def rda(rda):
    return "i am in Rwanda"

if __name__ == '__main__':
    app.run(debug=True)
