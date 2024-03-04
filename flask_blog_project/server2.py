from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import BlogPost,db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
app.config['SECRET_KEY'] = 'my_secret'

db.init_app(app)
migrate = Migrate(app, db) # This is the migration engine

# Create the database
with app.app_context():
    db.create_all()

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class myForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)], render_kw={"placeholder": "Name", "class":"form-control"})
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up', render_kw={"class":"btn btn-primary"})


@app.route('/')
def create_post():
    form = BlogPostForm()
    
    if form.validate_on_submit():
        post = BlogPost()
        form.populate_obj(post)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return '<h1>Post has been created!</h1>'


@app.route('/blog', methods=['GET', 'POST'])
def blog():
    form = BlogPostForm()
    if form.validate_on_submit():
        return '<h1>Post has been created!</h1>'
    return render_template('blog.html', form=form)