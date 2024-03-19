from flask import render_template
from core.posts import bp
#from core.models import Post
from core.extensions import db
from core.models.post import Post

@bp.route('/')
def index():
    return render_template('posts/index.html')

@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)