from app import app
from flask import render_template
from . import auth

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('login')
def login():
    return render_template('login.html')

