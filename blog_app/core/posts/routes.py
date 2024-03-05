from flask import render_template
from core.posts import bp

@bp.route('/')
def index():
    return render_template('posts/index.html')

@bp.route('/categories/')
def categories():
    return render_template('posts/categories.html')