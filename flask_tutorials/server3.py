from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Dummy data

blog_posts = {
    '1': {
        'title': 'Hello, World!',
        'content': 'This is the first blog post'
    },
    '2': {
        'title': 'The second post',
        'content': 'This is the second blog post'
    }

}

# Parser for handling Request data
parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help='Title of the blog post')
parser.add_argument('content', type=str, help='Content of the blog post')

class BlogPosts(Resource):
    def get(self):
        return jsonify(blog_posts)
    
    def post(self):
        args = parser.parse_args()
        blog_post_id = int(max(blog_posts.keys())) + 1
        blog_post_id = '%i' % blog_post_id
        blog_posts[blog_post_id] = {
            'title': args['title'],
            'content': args['content']
        }
        return jsonify(blog_posts[blog_post_id])
    
class BlogPost(Resource):
    def get(self, blog_post_id):
        if blog_post_id not in blog_posts:
            return 'Not found', 404
        return jsonify(blog_posts[blog_post_id])
    
    def put(self, blog_post_id):
        args = parser.parse_args()
        if blog_post_id not in blog_posts:
            return 'Not found', 404
        blog_posts[blog_post_id] = {
            'title': args['title'],
            'content': args['content']
        }
        return jsonify(blog_posts[blog_post_id])
    
    def delete(self, blog_post_id):
        if blog_post_id not in blog_posts:
            return 'Not found', 404
        del blog_posts[blog_post_id]
        return '', 204


# @app.route('/')
# def index():
#     return jsonify({'message': 'Hello, World!'})

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}
    
api.add_resource(HelloWorld, '/')
api.add_resource(BlogPosts, '/api/posts')
api.add_resource(BlogPost, '/api/posts/<blog_post_id>')


if __name__ == '__main__':
    app.run(debug=True)