from flask import jsonify
from flask.blueprints import Blueprint
from flask.typing import ResponseReturnValue

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/", methods=["POST"])
def main() -> ResponseReturnValue:
    return jsonify({"status": "ok"})
