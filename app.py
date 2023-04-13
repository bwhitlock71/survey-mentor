from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-questions"

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_route():

    question = satisfaction_survey.questions
    return render_template('base.html', questions=question)  

@app.route('/question')
def show_questions():
    return render_template('question.html')
    
   


