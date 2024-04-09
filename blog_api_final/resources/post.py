from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import PostModel, CategoryModel
from schemas import PostSchema, PostUpdateSchema, PostsCategoriesSchema


# blp = Blueprint("Stores", "stores", description="Operations on stores")
blp = Blueprint("Posts", "posts", description="Operations on posts")


@blp.route("/post/<string:post_id>")
class Post(MethodView):
    @blp.response(200, PostSchema)
    def get(self, post_id):
        post = PostModel.query.get_or_404(post_id)
        return post

    @blp.arguments(PostUpdateSchema)
    @blp.response(200, PostSchema)
    def put(self, post_data, post_id):
        post = PostModel.query.get_or_404(post_id)

        post.title = post_data["title"]
        post.content = post_data["content"]

        db.session.add(post)
        db.session.commit()

        return post

    def delete(self, post_id):
        post = PostModel.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return {"message": "Post deleted"}, 200
    

@blp.route("/post")
class PostList(MethodView):
    @blp.response(200, PostSchema(many=True))
    def get(self):
        return PostModel.query.all()

    @blp.arguments(PostSchema)
    @blp.response(201, PostSchema)
    def post(self, post_data):
        post = PostModel(**post_data)
        try:
            db.session.add(post)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A post with that title already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the post.")

        return post
    

@blp.route("/post/<string:post_id>/category")
class CategoriesInPost(MethodView):
    @blp.response(200, PostsCategoriesSchema(many=True))
    def get(self, post_id):
        post = PostModel.query.get_or_404(post_id)

        return post.categories.all()
    
    @blp.arguments(PostsCategoriesSchema)
    @blp.response(201, PostsCategoriesSchema)
    def post(self, category_data, post_id):
        post = PostModel.query.get_or_404(post_id)

        category = CategoryModel.query.get_or_404(category_data["category_id"])
        post.categories.append(category)

        try:
            db.session.add(post)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the category.")

        return category
    

@blp.route("/post/<string:post_id>/category/<string:category_id>")
class LinkCategoriesToPost(MethodView):
    @blp.response(201, PostsCategoriesSchema)
    def post(self, post_id, category_id):
        post = PostModel.query.get_or_404(post_id)
        category = CategoryModel.query.get_or_404(category_id)

        post.categories.append(category)

        try:
            db.session.add(post)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the category.")

        return category

    @blp.response(200, PostsCategoriesSchema)
    def delete(self, post_id, category_id):
        post = PostModel.query.get_or_404(post_id)
        category = CategoryModel.query.get_or_404(category_id)

        post.categories.remove(category)

        try:
            db.session.add(post)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the category.")

        return category
    
