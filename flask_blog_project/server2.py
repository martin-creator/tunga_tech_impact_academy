from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret'

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class myForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)], render_kw={"placeholder": "Name", "class":"form-control"})
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog', methods=['GET', 'POST'])
def blog():
    form = BlogPostForm()
    if form.validate_on_submit():
        return '<h1>Post has been created!</h1>'
    return render_template('blog.html', form=form)