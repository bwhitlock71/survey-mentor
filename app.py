from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-questions"

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_route():
    return render_template('base.html')  

@app.route('/question', methods=["POST"])
def show_questions():
      question = satisfaction_survey.questions
      return render_template('question.html',questions=question)
    
   


