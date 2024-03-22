from core.blog import bp
from flask_login import login_required, current_user, login_user, logout_user
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
import logging
from core.models.blog import Blog

# title = db.Column(db.String(150))
#     header_image = db.Column(db.String(150))
#     content = db.Column(db.Text)
#     author = db.Column(db.String(150))
#     date_posted = db.Column(db.DateTime)
#     category = db.Column(db.String(150)) 


@bp.route('/')
def index():
    return render_template('blog/index.html')

@bp.route('/create', methods=['GET'])
def create_blog_page():
    return render_template('blog/create_blog.html')

@bp.route('/create', methods=['POST'])
def create_blog():
        
        # Handle exception if the blog is not created
    try:
        new_blog = Blog(title=request.form['title'],
                        header_image=request.form['image'],
                        content=request.form['content'],
                        author=request.form['author'],
                        date_posted=request.form['date'],
                        category=request.form['category'])
        db.session.add(new_blog)
        db.session.commit()
        flash('Blog created successfully', 'success')
        return redirect(url_for('blog.create_blog_page'))
    except:
        flash('Error creating blog')


        # log tthe actual error for debugging

        logging.error('Error creating blog', exc_info=True)

        return redirect(url_for('blog.create_blog_page'))
    

    # flash('Error creating blog')
    # return redirect(url_for('blog.create_blog_page'))

   
    #return 'Blog created successfully'
    
    
    

@bp.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html', name=current_user.name, email=current_user.email, id=current_user.id, password=current_user.password)