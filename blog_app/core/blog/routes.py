from core.blog import bp
from flask_login import login_required, current_user
from flask import render_template
from core.extensions import db
from core.models.blog import Blog


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/create', methods=['GET'])
def create_blog_page():
    return render_template('blog/create_blog.html')

@bp.route('/create')
def create_blog():
    blog = Blog(title='My Blog', user_id=1)
    db.session.add(blog)
    db.session.commit()
    return 'Blog created'

@bp.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html', name=current_user.name, email=current_user.email, id=current_user.id, password=current_user.password)