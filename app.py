from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-questions"

debug = DebugToolbarExtension(app)

responses = []

"""
you were using the question variable in the base.html template,
but not passing the questions param in. i added this in.
You were also only displaying the object reference, not the values on it
"""
@app.route('/')
def show_route():
    question = satisfaction_survey.questions
    return render_template('base.html', questions=question)

"""
This was using POST before. be sure to recognize the difference between
GET and POST
In order to get individual questions, you want to do something like
@app.route('/question/<id>', methods=["GET"])
def show_questions(id)
this will make the id available as a arg passed into your function
"""
@app.route('/question', methods=["GET"])
def show_questions():
    question = satisfaction_survey.questions
    return render_template('question.html', questions=question)
