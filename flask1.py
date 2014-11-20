#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask, make_response
#from flask import request



app= Flask(__name__)

@app.route('/')

def index():
	#user_agent=request.headers.get('User-Agent')
	return make_response("<h1> Your browser </h1>")

@app.route('/<kigali>')

def rda(kigali):
    response= make_response("i am in capital of Rwanda")
    return response

@app.route('/greet/<name>')

def greet(name):
    response=make_response("<h1>Mwaramutse, %s how is home?<h1>" % name)
    return response

@app.route('/counter/<int:num>')

def counter(num):
	dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
	response= make_response('Number %s' % dict.get( num,'unknown'))
	return response


if __name__ == '__main__':
    app.run(debug=True)
