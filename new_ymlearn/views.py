"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from new_ymlearn import app
import psycopg2
import os


#Connect to DB in Heroku
#DATABASE_URL = os.environ['DATABASE_URL']
DATABASE_URL = 'postgres://svqsyxjufbvthi:c72117284b2863babb395540da2b749fb1e5bdc25845378ed8c69edbf1e0db4f@ec2-54-74-14-109.eu-west-1.compute.amazonaws.com:5432/dnvhkb81c6gu3'
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()




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

    
    cur.execute("SELECT * FROM public.topics")

    topics = cur.fetchall()

    #listoutput=[i[0] for i in topics]

   
    """Renders the about page."""
    return render_template(
        'GCSE.html',
        topics = topics,
        title='GCSE Home',
        default = 'Number'
    )

@app.route('/topic/<id>')

def topics(id):

    #Query to return topic name 
    topic_header = conn.cursor()

    topic_header.execute("select distinct topic from public.topics t where id =value".replace("value",id))

    topic_name = topic_header.fetchone()


    #Query to return sub topics
    all_topics = conn.cursor()

    all_topics.execute("select * from public.topics t inner join public.subtopics s on t.id = s.topic_id where topic_id = value".replace("value",id))

    subtopic = all_topics.fetchall()



    return render_template('topic.html', subtopic = subtopic, topic_name = topic_name)




@app.route('/learn')

def learn():


    return render_template('learn.html')

