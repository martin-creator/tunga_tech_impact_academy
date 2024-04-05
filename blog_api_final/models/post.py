from db import db


class PostModel(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable=False)

    author = db.relationship("AuthorModel", back_populates="posts")
    categories = db.relationship("CategoryModel", secondary="posts_categories", back_populates="posts")