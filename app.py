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

#Creating custom error pages
#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("not_found.html"), 404

#Internal Server Error
@app.errorhandler(404)
def page_500(e):
    return render_template("error_500.html"), 500