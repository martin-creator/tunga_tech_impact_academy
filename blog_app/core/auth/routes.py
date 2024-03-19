from core.auth import bp
from flask import render_template


@bp.route('/login')
def login():
    render_template('auth/login.html')

@bp.route('/signup')
def signup():
    return render_template('auth/signup.html')

@bp.route('/logout')
def logout():
    return render_template('auth/logout.html')