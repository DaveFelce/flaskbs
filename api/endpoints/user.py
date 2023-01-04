from typing import Any

from flask import Blueprint, request

bp = Blueprint("user", __name__)


@bp.route("/user/<name>", methods=("GET", "POST"))
def user(name: str) -> Any:
    if request.method == "GET":
        return f"Hello, {name}"
