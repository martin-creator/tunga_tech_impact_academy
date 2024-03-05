from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models import BlogPost,db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
app.config['SECRET_KEY'] = 'my_secret'

app.register_blueprint(auth)
app.register_blueprint(blog)

login_manager = LoginManager()

db.init_app(app)
migrate = Migrate(app, db) # This is the migration engine

# Create the database
with app.app_context():
    db.create_all()

login_manager.init_app(app)

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

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required # Authorization implementation since the user must be logged in to access the home page
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('You have been logged in!', 'success')
            return redirect(url_for('blog'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)