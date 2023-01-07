from typing import Any

from flask import Blueprint
from flask_pydantic import validate
from flask_restful import Api, Resource
from sqlalchemy.future import select

from flaskbs.db import db
from flaskbs.models import User
from flaskbs.schemas.user import UserQueryResponseSchema

bp = Blueprint("user", __name__)
api = Api(bp)


class UserResource(Resource):
    @validate()
    def get(self, username: str) -> Any:
        user_email = db.session.execute(select(User.email).where(User.username == username)).scalar_one_or_none()

        return UserQueryResponseSchema(greeting=f"hello, {user_email}")


api.add_resource(UserResource, "/user/<username>")
