from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#Create flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret key no one is supposed to know'

#Creating a form class
class nameForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

#Create a route decorator
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

@app.route('/name', methods=['GET', 'POST']) 
def name():
    name = None
    form = nameForm()
    # Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully")
    return render_template("name.html", name = name, form=form)

#Creating custom error pages
#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("not_found.html"), 404

#Internal Server Error
@app.errorhandler(404)
def page_500(e):
    return render_template("error_500.html"), 500