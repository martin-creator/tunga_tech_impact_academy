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

@app.route('/articles', method=['GET'])
def get_articles():
    """
    This function takes no arguments and returns a string.
    """
    return 'List of all articles'


@app.route('/articles', method=['POST'])
def create_article():
    """
    This function takes no arguments and returns a string.
    """
    return 'Create a new article'

@app.route('/articles/<int:article_id>', method=['GET'])
def get_article(article_id):
    """
    This function takes an integer as an argument and returns a string.
    """
    return f'View article with id {article_id}'


@app.route('/articles/<int:article_id>', method=['PUT'])
def update_article(article_id):
    """
    This function takes an integer as an argument and returns a string.
    """
    return f'Update article with id {article_id}'


@app.route('/articles/<int:article_id>', method=['DELETE'])
def delete_article(article_id):
    """
    This function takes an integer as an argument and returns a string.
    """
    return f'Delete article with id {article_id}'

@app.route('/articles/<int:article_id>/comments', method=['PATCH'])
def update_comments(article_id):
    """
    This function takes an integer as an argument and returns a string.
    """
    return f'Update comments for article with id {article_id}'

# Pass multiple http methods
@app.route('/articles/<int:article_id>/comments', method=['GET', 'POST'])
def get_or_create_comments(article_id):
    """
    This function takes an integer as an argument and returns a string.
    """
    return f'Get or create comments for article with id {article_id}'



# # Generating a url for usr_profile
# url = url_for('user_profile', username='michael')
# print(url)

if __name__ == '__main__':
    app.run(debug=True)