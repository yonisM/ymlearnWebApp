"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from new_ymlearn import app



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
    """Renders the about page."""

    return render_template(
        'GCSE.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )





