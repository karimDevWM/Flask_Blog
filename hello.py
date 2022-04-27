# import os
# from dotenv import load_dotenv
from crypt import methods
from unicodedata import name
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
import sqlalchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

## create flask instance, (__name__) helps flask to find static files in the project
app = Flask(__name__)

# Add Database

# mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/our_users2'

# sqlite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initialize the database
db = SQLAlchemy(app)
# create the model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
# create a string
def __repr__(self):
    return '<Name %r>' % self.name



# set env variable
if app.config['ENV'] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config['ENV'] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")
    
print(app.config['ENV'])

if __name__ == '__main__':
    app.run()

# create a form class for database
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")

# create a form class
class NamerForm(FlaskForm):
    name = StringField("what's your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

## create a route decorator
# @app.route('/')
# def index():
#     return "<h1>Hello World !</h1>"

'''
    filters List :
safe
capitalize
lower
upper
title
trim
striptags
'''

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data,
                         email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        # clear the form
        form.name.data = ''
        form.email.data = ''
        flash("user added successfully !")
    # hold database data ordered by there date_added in our_users variable
    our_users = Users.query.order_by(Users.date_added)
    return render_template("add_user.html", form=form, 
                                            name=name, 
                                            # fetch our_users table variable in the rendered template
                                            our_users = our_users)

@app.route('/')
def index():
    # print(app.config['ENV'])
    first_name = 'Karim'
    stuff = 'this is <strong>bold</strong> text'
    favorite_pizza = ["Pepperoni", "Cheeze", "Mushrooms", 41]
    #                                    things accessed    function variables
                                        # in the web page
    return render_template("index.html", first_name =       first_name,
                                        stuff =             stuff,
                                        favorite_pizza =    favorite_pizza)

        ## localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    # return "<h1>Hello {}!!!</h1>".format(name)
    #                                   url parameter          function variable
    return render_template("user.html", user_name=             name)

# create custom error pages

    # invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

    # internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# create name form
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form submitted successfully !")
    
    return render_template("name.html",
                           name = name,
                           form = form
                           )
    