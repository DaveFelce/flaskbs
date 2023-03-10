from http import HTTPStatus
from typing import Any

from flask import Blueprint, abort
from flask_pydantic import validate
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from flaskbs.db import db
from flaskbs.models import User
from flaskbs.schemas.user import GetUserResponseSchema, PostUserBodySchema

bp = Blueprint("user", __name__)
api = Api(bp)


class UserGetResource(Resource):
    @validate()
    def get(self, username: str) -> Any:
        user_email = db.session.execute(select(User.email).where(User.username == username)).scalar_one_or_none()

        if user_email is None:
            abort(HTTPStatus.NOT_FOUND, description="User not found")

        return GetUserResponseSchema(greeting=f"hello, {user_email}")


class UserPostResource(Resource):
    @validate()
    def post(self, body: PostUserBodySchema) -> Any:
        username = body.username
        email = body.email

        user = User(username=username, email=email)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            abort(HTTPStatus.CONFLICT, description="User already exists (duplicate name)")

        return {}


api.add_resource(UserPostResource, "/user")
api.add_resource(UserGetResource, "/user/<username>")
