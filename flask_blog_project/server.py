from flask import Flask, url_for, request, jsonify, redirect, make_response

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


@app.route('/example', methods=['GET', 'POST'])
def example():
    """
    This function takes no arguments and returns a string.
    """
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are using GET'
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    This function takes no arguments and returns a string.
    """
    username = request.form.get('username')
    password = request.form.get('password')
    # Process the username and password

@app.route('/search', methods=['GET'])
def search():
    """
    This function takes no arguments and returns a string.

    Example of url: /search?q=flask
    e
    """
    query = request.args.get('q')
    # Process the query

@app.route('/json_data', methods=['POST'])
def json_data():
    """
    This function takes no arguments and returns a string.
    """
    data = request.json
    # Process the json data

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    This function takes no arguments and returns a string.
    """
    file = request.files['file']
    # Process the file

@app.route('/cookies', methods=['GET'])
def cookies():
    """
    This function takes no arguments and returns a string.
    """
    cookie = request.cookies.get('cookie_name')
    # Process the cookie

@app.route('/redirect')
def redirect():
    """
    This function takes no arguments and returns a string.
    """
    return redirect(url_for('index'))

@app.route('/get_path')
def get_path():
    """
    This function takes no arguments and returns a string.
    """
    return request.path

@app.route('/get_full_path')
def get_full_path():
    """
    This function takes no arguments and returns a string.
    """
    return request.full_path

@app.route('/headers')
def headers():
    """
    This function takes no arguments and returns a string.
    """
    return str(request.headers)

# Returning responses

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>', 200

@app.route('/api/data')
def api_data():
    data = {
        'name': 'Michael',
        'age': 25
    }
    return jsonify(data)

@app.route('/redirect')
def redirect():
    return redirect(url_for('index'))

@app.route('/set_custom_cookie')
def set_custom_cookie():
    response = "Cookie has been set"
    resp = make_response(response)
    resp.set_cookie('custom_cookie', 'flask')
    return resp

@app.route('/render_template')
def render_template():
    return render_template('index.html')


    

# # Generating a url for usr_profile
# url = url_for('user_profile', username='michael')
# print(url)

if __name__ == '__main__':
    app.run(debug=True)