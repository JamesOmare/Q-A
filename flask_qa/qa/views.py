from flask import Blueprint, render_template
from ..utils import db
from ..models.question import Question

q_a = Blueprint('q_a', __name__)

@q_a.route('/')
def index():
    return render_template('home.html')

@q_a.route('/ask')
def ask():
    return render_template('ask.html')

@q_a.route('/answer')
def answer():
    return render_template('answer.html')

@q_a.route('/question')
def question():
    return render_template('question.html')


@q_a.route('/unanswered')
def unanswered():
    return render_template('unanswered.html')

@q_a.route('/users')
def users():
    return render_template('users.html')