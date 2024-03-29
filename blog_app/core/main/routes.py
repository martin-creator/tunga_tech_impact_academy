from core.main import bp
from flask_login import login_required, current_user
from flask import render_template


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html', name=current_user.name, email=current_user.email, id=current_user.id, password=current_user.password)