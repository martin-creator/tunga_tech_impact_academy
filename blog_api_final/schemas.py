from marshmallow import Schema, fields

class PlainPostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)

class PlainCategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class PlainAuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    email = fields.Email()

class PostSchema(PlainPostSchema):
    author_id = fields.Int(required=True, load_only=True)
    author = fields.Nested(PlainAuthorSchema(), dump_only=True)
    categories = fields.List(fields.Nested(PlainCategorySchema()), dump_only=True)

class PostUpdateSchema(Schema):
    title = fields.Str()
    content = fields.Str()

class CategorySchema(PlainCategorySchema):
    posts = fields.List(fields.Nested(PlainPostSchema()), dump_only=True)

class PostsCategoriesSchema(Schema):
    id = fields.Int(dump_only=True)
    post_id = fields.Int(required=True, load_only=True)
    category_id = fields.Int(required=True, load_only=True)

class AuthorSchema(PlainAuthorSchema):
    posts = fields.List(fields.Nested(PlainPostSchema()), dump_only=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    email = fields.Email(required=True)

class UserRegisterSchema(UserSchema):
    pass



class UserRegisterSchema(UserSchema):
    email = fields.Str(required=True)
