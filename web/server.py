#!/bin/env python
import os,sys,time,requests, json, pymongo, gc
from flask import Flask, request, make_response, jsonify, render_template, redirect

app = Flask("Web Server for ChatRooms", static_url_path='/static')

db=pymongo.MongoClient()["Group_Chat"]

title="The Chat Room"

def counthits(func):
    def wrapper(*args, **kwargs):
	remote=db["HITS"].find_one({"ip":request.remote_addr})
	if remote:
		hitsno=remote["HITS_NO"]
		db["HITS"].find_one_and_update({"ip":request.remote_addr},{"$set":{"HITS_NO":hits_no}})
	db.find_and
        result = func(*args, **kwargs)
        return result
    return wrapper



@app.errorhandler(404)
@counthits
def _404(e):
	return render_template('404.html'), 404


@app.route("/",methods=["GET"])
@counthits
def root():
	return render_template('layout.html',title=title), 200


@app.route("/home",methods=["GET"])
def home():
	return app.send_static_file('home.html')

@app.route("/index",methods=["GET"])
def index():
	return render_template('index.html',title=title,nickname=nickname), 200

@app.route("/login",methods=["GET"])
def login():
	return app.send_static_file('login.html')

@app.route("/accept/login",methods=["POST"])
def accept_login():
	print("login",request.json)
	nickname=request.json.get("user","")
	password=request.json.get("pass","")
	for user in users:
		if user["nickname"]==nickname and user["password"]==password:
			pass#user is logged in
	return redirect("/", code=302)

@app.route("/accept/logout",methods=["POST"])
def accept_logout():
	print("logout",request.json)
	return redirect("/", code=302)

@app.route("/register",methods=["GET"])
def register():
	return app.send_static_file('register.html')

@app.route("/accept/register",methods=["POST"])
def accept_register():
	print("register",request.json)
	return json.dumps([])

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=30002, threaded=True, use_reloader=False)
