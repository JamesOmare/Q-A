from crypt import methods
from flask import Blueprint, redirect, render_template, url_for, request
from ..models.user import User
from ..utils import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        unhashed_password = request.form['password']

        user = User(
            name = name, 
            unhashed_password = unhashed_password, 
            admin = True, 
            expert = False
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('register.html')
