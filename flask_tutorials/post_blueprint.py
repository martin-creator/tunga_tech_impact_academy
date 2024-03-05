from flask import Blueprint, render_template, request, redirect, url_for, flash


post = Blueprint('post', __name__)


@post.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        flash('Post created successfully', 'success')
        return redirect(url_for('post.create_post'))
    return render_template('create_post.html')

