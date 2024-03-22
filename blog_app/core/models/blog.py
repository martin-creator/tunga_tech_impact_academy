from core.extensions import db

class Blog(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    header_image = db.Column(db.String(150))
    content = db.Column(db.Text)
    author = db.Column(db.String(150))
    date_posted = db.Column(db.String(150))
    category = db.Column(db.String(150))


    def __repr__(self):
        return f'<Blog "{self.title}">'