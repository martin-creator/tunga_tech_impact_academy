# # Basic error handling

# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def server_error(error):
#     return render_template('500.html'), 500

# # Custom error handling

# class MyCustomError(Exception):
#     pass

# @app.errorhandler(MyCustomError)
# def handle_custom_error(error):
#     return render_template('my_custom_error.html'), 500

# # Error handling for specific blueprints

# from core.posts import bp as posts_bp

# @posts_bp.errorhandler(404)
# def not_found(error):
#     return render_template('posts/404.html'), 404

# @posts_bp.errorhandler(500)
# def server_error(error):
#     return render_template('posts/500.html'), 500

# # Error handling for specific routes

# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

# # Utilizng response class to handle errors

# from flask import Response

# @app.errorhandler(404)
# def not_found(error):
#     return Response('<h3>Not found</h3>', status=404)


