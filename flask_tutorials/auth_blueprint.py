from Flask import Blueprint, render_template, redirect, url_for, flash, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

