from blog_api.db import db



class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")

    # lazy="dynamic" is used to tell SQLAlchemy to not load the items automatically
    # This is useful when we have a large number of items in the database
    # and we don't want to load all of them at once
    # We can use the items relationship to query the items in the database
    # Example: store.items.all() will return all the items in the store
    # store.items.filter_by(name="item_name") will return the item with the given name
    # store.items.filter_by(price=10.0) will return the items with the given price