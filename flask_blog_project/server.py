from flask import Flask, url_for

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

@app.route('/user/<username>')
def user_profile(username):
    """
    This function takes a string as an argument and returns a string.
    """
    return f"User profile for {username}"

# # Generating a url for usr_profile
# url = url_for('user_profile', username='michael')
# print(url)

if __name__ == '__main__':
    app.run(debug=True)