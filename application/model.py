from .db import db


class UserModel(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    cpf = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True)
    birth_date = db.DateTimeField(required=True)
