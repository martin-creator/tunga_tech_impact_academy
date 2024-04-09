from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import CategoryModel
from schemas import CategorySchema

# blp = Blueprint("Items", "items", description="Operations on items")
blp = Blueprint("Categories", "categories", description="Operations on categories")

@blp.route("/category/<string:category_id>")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, category_id):
        category = CategoryModel.query.get_or_404(category_id)
        return category

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def put(self, category_data, category_id):
        category = CategoryModel.query.get_or_404(category_id)

        category.name = category_data["name"]

        db.session.add(category)
        db.session.commit()

        return category

    def delete(self, category_id):
        category = CategoryModel.query.get_or_404(category_id)
        db.session.delete(category)
        db.session.commit()
        return {"message": "Category deleted"}, 200
    

@blp.route("/category")
class CategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()

    @blp.arguments(CategorySchema)
    @blp.response(201, CategorySchema)
    def post(self, category_data):
        category = CategoryModel(**category_data)
        try:
            db.session.add(category)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the category.")
        return category
    

# from flask.views import MethodView


# @blp.route("/item/<string:item_id>")
# class Item(MethodView):
#     @jwt_required()
#     @blp.response(200, ItemSchema)
#     def get(self, item_id):
#         item = ItemModel.query.get_or_404(item_id)
#         return item

#     @jwt_required()
#     def delete(self, item_id):
#         jwt = get_jwt()
#         if not jwt.get("is_admin"):
#             abort(401, message="Admin privilege required.")

#         item = ItemModel.query.get_or_404(item_id)
#         db.session.delete(item)
#         db.session.commit()
#         return {"message": "Item deleted."}

#     @blp.arguments(ItemUpdateSchema)
#     @blp.response(200, ItemSchema)
#     def put(self, item_data, item_id):
#         item = ItemModel.query.get(item_id)

#         if item:
#             item.price = item_data["price"]
#             item.name = item_data["name"]
#         else:
#             item = ItemModel(id=item_id, **item_data)

#         db.session.add(item)
#         db.session.commit()

#         return item


# @blp.route("/item")
# class ItemList(MethodView):
#     @jwt_required()
#     @blp.response(200, ItemSchema(many=True))
#     def get(self):
#         return ItemModel.query.all()

#     @jwt_required(fresh=True)
#     @blp.arguments(ItemSchema)
#     @blp.response(201, ItemSchema)
#     def post(self, item_data):
#         item = ItemModel(**item_data)

#         try:
#             db.session.add(item)
#             db.session.commit()
#         except SQLAlchemyError:
#             abort(500, message="An error occurred while inserting the item.")

#         return item
