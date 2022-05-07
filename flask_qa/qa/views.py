from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from ..utils import db
from ..models.question import Question
from ..models.user import User

q_a = Blueprint('q_a', __name__)

@q_a.route('/')
def index():
    return render_template('home.html')

@q_a.route('/ask', methods = ['POST', 'GET'])
@login_required
def ask():
    if request.method == 'POST':
        question_ = request.form['question']
        expert = request.form['expert']

        question = Question(
            question = question_, 
            expert_id = expert, 
            asked_by_id = current_user.id 
        )

        db.session.add(question)
        db.session.commit()

        return redirect(url_for('q_a.index'))
    experts = User.query.filter_by(expert = True).all()

    context = {

        'experts' : experts

    }

    return render_template('ask.html', **context)

@q_a.route('/answer/<int:question_id>')
def answer(question_id):
    return render_template('answer.html')

@q_a.route('/question')
def question():
    return render_template('question.html')


@q_a.route('/unanswered')
@login_required
def unanswered():
    unanswered_questions = Question.query.filter_by(expert_id = current_user.id).filter(Question.answer == None).all()

    context = {
        'unanswered_questions': unanswered_questions
    }

    return render_template('unanswered.html', **context)

@q_a.route('/users')
def users():
    return render_template('users.html')