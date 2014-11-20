#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask


app= Flask(__name__)

@app.route('/')

def index():
    return "i am in Rwanda"

@app.route('/<kigali>')

def rda(kigali):
    return "i am in capital of Rwanda"

@app.route('/greet/<name>')

def greet(name):
    return "<h1>Mwaramutse, %s how is home?<h1>" % name

@app.route('/counter/<int:num>')

def counter(num):
	dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
	return 'Number %s' % dict.get( num,'unknown')


if __name__ == '__main__':
    app.run(debug=True)
