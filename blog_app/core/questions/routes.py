from flask import render_template
from core.questions import bp
from core.models.question import Question

@bp.route('/')
def index():
    questions = Question.query.all()
    return render_template('questions/index.html', questions=questions)