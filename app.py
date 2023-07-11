# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Lily" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def hello():

    name = "Andrew" 
    age = "43" 

# define the route to mother webpage
@app.route("/mother")
def hi():

    name = "Amy" 
    age = "41" 
# define the route to friends webpage
@app.route("/friend")
def house():

    name = "Sammy" 
    age = "14" 
# add other routes, if you want







