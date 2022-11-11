from flask import Flask, render_template

#Create flask instance
app = Flask(__name__)

#Create a route decorator
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)