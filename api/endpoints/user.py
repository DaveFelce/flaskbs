from typing import Any

from flask import Blueprint
from flask_pydantic import validate
from flask_restful import Api, Resource

from schemas.user import UserQueryResponseSchema

bp = Blueprint("user", __name__)
api = Api(bp)


class User(Resource):
    @validate()
    def get(self, username: str) -> Any:
        return UserQueryResponseSchema(greeting=f"hello, {username}")


api.add_resource(User, "/user/<username>")
