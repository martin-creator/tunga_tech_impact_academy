from flask import Flask, render_template
from jinja2 import Template
import datetime

app = Flask(__name__)

@app.template_filter('format_date')
def format_date(date, format_string):
    return date.strftime(format_string)

app.jinja_env.globals.update(format_date=format_date)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.datetime.now())