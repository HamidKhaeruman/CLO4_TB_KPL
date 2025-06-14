# app.py

from flask import Flask, render_template, request, redirect, url_for, session
from src.state_machine import StateMachine, QuizState
from src.quiz_manager import QuizManager
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure session

def get_quiz_manager():
    if 'quiz_manager' not in session:
        session['quiz_manager'] = {}
    if not hasattr(app, 'quiz_manager'):
        app.quiz_manager = QuizManager()
    return app.quiz_manager

@app.route('/')
def home():
    session.clear()  # Secure: clear session on home
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    #clean code untuk quiz_manager
    quiz_manager = get_quiz_manager()
    if request.method == 'POST':
        answer = request.form.get('answer', '')
        quiz_manager.answer_current(answer)
        if quiz_manager.is_finished():
            return redirect(url_for('result'))
    else:
        quiz_manager.start_quiz()
    question = quiz_manager.get_current_question()
    if question:
        return render_template('quiz.html', question=question, index=quiz_manager.current_index+1, total=len(quiz_manager.questions))
    else:
        return redirect(url_for('result'))

@app.route('/result')
def result():
    quiz_manager = get_quiz_manager()
    return render_template('result.html', score=quiz_manager.get_score(), results=quiz_manager.get_result(), total=len(quiz_manager.questions))

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('home.html'), 404

if __name__ == '__main__':
    app.run(debug=True)