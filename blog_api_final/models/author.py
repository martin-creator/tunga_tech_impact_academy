from db import db

class AuthorModel(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    # password = db.Column(db.String(256), nullable=False)

    posts = db.relationship("PostModel", back_populates="author")
    
