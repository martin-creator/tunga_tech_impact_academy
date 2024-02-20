from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/post/<int:post_id>')
def view_post(post_id):
    """
    This function takes an integer as an argument and returns a string.
    """
    return f"Viewing post with id {post_id}"

if __name__ == '__main__':
    app.run(debug=True)