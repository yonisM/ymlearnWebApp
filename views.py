"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from new_ymlearn import app
import psycopg2
import os


#Connect to DB in Heroku
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')






@app.route('/')
@app.route('/login')
def login():

    return render_template('login.html')



@app.route('/registration')
def registration():

    return render_template('registration.html')



@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'home.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/account')
def account():
    """Renders the contact page."""
    return render_template(
        'account.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/GCSE')
def GCSE():

    cur = conn.cursor()
    topics = cur.execute("SELECT * FROM public.topics;")
    




    """Renders the about page."""
    return render_template(
        'GCSE.html',
        title='About',
        topics = topics
    )





