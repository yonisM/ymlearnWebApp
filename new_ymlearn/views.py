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

@app.route('/topic/<id>', methods=['GET','POST'])

def topics(id):

    #Query to return topic name 
    topic_header = conn.cursor()
    topic_header.execute("select distinct topic from public.topics t where id =value".replace("value",id))
    topic_name = topic_header.fetchone()


    #Query to return sub topics
    all_topics = conn.cursor()
    all_topics.execute("select * from public.topics t inner join public.subtopics s on t.id = s.topic_id where topic_id = value".replace("value",id))
    subtopic = all_topics.fetchall()

    
    
    #Query to return learning objectives
    learning_objective = conn.cursor()
    learning_objective.execute("select learning_objectives, lo.sub_topic_id from public.subtopics s inner join public.learning_objective lo on s.sub_topic_id = lo.sub_topic_id where topic_id =value".replace("value", id))
    learning_objectives = learning_objective.fetchall()





    return render_template('topic.html', subtopic = subtopic, topic_name = topic_name, learning_objectives = learning_objectives)









@app.route('/learn/<sub_topic_id>')

def learn(sub_topic_id):

    #Query to return learning objectives
    learning_objective = conn.cursor()

    learning_objective.execute("select * from public.learning_objective where sub_topic_id = value".replace("value", sub_topic_id))

    learning_objectives = learning_objective.fetchall()


    #Query to return topic name 
    topic_header = conn.cursor()

    topic_header.execute("select sub_topic from public.subtopics s inner join learning_objective lo on s.sub_topic_id = lo.sub_topic_id where lo.sub_topic_id = value limit 1".replace("value",sub_topic_id))

    topic_name = topic_header.fetchone()

    return render_template('learn.html', learning_objectives = learning_objectives, topic_name = topic_name )
