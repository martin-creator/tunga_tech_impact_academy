from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
# from models import TagModel, StoreModel, ItemModel
from models import AuthorModel
from schemas import AuthorSchema

# blp = Blueprint("Tags", "tags", description="Operations on tags")
blp = Blueprint("Authors", "authors", description="Operations on authors")


@blp.route("/author/<string:author_id>")
class Author(MethodView):
    @blp.response(200, AuthorSchema)
    def get(self, author_id):
        author = AuthorModel.query.get_or_404(author_id)
        return author

    @blp.arguments(AuthorSchema)
    @blp.response(200, AuthorSchema)
    def put(self, author_data, author_id):
        author = AuthorModel.query.get_or_404(author_id)

        author.name = author_data["name"]
        author.email = author_data["email"]

        db.session.add(author)
        db.session.commit()

        return author

    def delete(self, author_id):
        author = AuthorModel.query.get_or_404(author_id)
        db.session.delete(author)
        db.session.commit()
        return {"message": "Author deleted"}, 200
    

@blp.route("/author")
class AuthorList(MethodView):
    @blp.response(200, AuthorSchema(many=True))
    def get(self):
        return AuthorModel.query.all()

    @blp.arguments(AuthorSchema)
    @blp.response(201, AuthorSchema)
    def post(self, author_data):
        author = AuthorModel(**author_data)
        try:
            db.session.add(author)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the author.")
        return author
    




# @blp.route("/store/<string:store_id>/tag")
# class TagsInStore(MethodView):
#     @blp.response(200, TagSchema(many=True))
#     def get(self, store_id):
#         store = StoreModel.query.get_or_404(store_id)

#         return store.tags.all()  # lazy="dynamic" means 'tags' is a query

#     @blp.arguments(TagSchema)
#     @blp.response(201, TagSchema)
#     def post(self, tag_data, store_id):
#         if TagModel.query.filter(TagModel.store_id == store_id).first():
#             abort(400, message="A tag with that name already exists in that store.")

#         tag = TagModel(**tag_data, store_id=store_id)

#         try:
#             db.session.add(tag)
#             db.session.commit()
#         except SQLAlchemyError as e:
#             abort(
#                 500,
#                 message=str(e),
#             )

#         return tag


# @blp.route("/item/<string:item_id>/tag/<string:tag_id>")
# class LinkTagsToItem(MethodView):
#     @blp.response(201, TagSchema)
#     def post(self, item_id, tag_id):
#         item = ItemModel.query.get_or_404(item_id)
#         tag = TagModel.query.get_or_404(tag_id)

#         item.tags.append(tag)

#         try:
#             db.session.add(item)
#             db.session.commit()
#         except SQLAlchemyError:
#             abort(500, message="An error occurred while inserting the tag.")

#         return tag

#     @blp.response(200, TagAndItemSchema)
#     def delete(self, item_id, tag_id):
#         item = ItemModel.query.get_or_404(item_id)
#         tag = TagModel.query.get_or_404(tag_id)

#         item.tags.remove(tag)

#         try:
#             db.session.add(item)
#             db.session.commit()
#         except SQLAlchemyError:
#             abort(500, message="An error occurred while inserting the tag.")

#         return {"message": "Item removed from tag", "item": item, "tag": tag}


# @blp.route("/tag/<string:tag_id>")
# class Tag(MethodView):
#     @blp.response(200, TagSchema)
#     def get(self, tag_id):
#         tag = TagModel.query.get_or_404(tag_id)
#         return tag

#     @blp.response(
#         202,
#         description="Deletes a tag if no item is tagged with it.",
#         example={"message": "Tag deleted."},
#     )
#     @blp.alt_response(404, description="Tag not found.")
#     @blp.alt_response(
#         400,
#         description="Returned if the tag is assigned to one or more items. In this case, the tag is not deleted.",
#     )
#     def delete(self, tag_id):
#         tag = TagModel.query.get_or_404(tag_id)

#         if not tag.items:
#             db.session.delete(tag)
#             db.session.commit()
#             return {"message": "Tag deleted."}
#         abort(
#             400,
#             message="Could not delete tag. Make sure tag is not associated with any items, then try again.",  # noqa: E501
#         )
