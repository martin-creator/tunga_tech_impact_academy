from db import db


class PostsCategories(db.Model):
    __tablename__ = "posts_categories"

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))