from typing import Any

from flask import Blueprint
from flask_pydantic import validate

from schemas.user import UserQueryResponseSchema

bp = Blueprint("user", __name__)


@bp.route("/user/<username>", methods=["GET"])
@validate()
def user(username: str) -> Any:
    return UserQueryResponseSchema(greeting=f"hello, {username}")
