from flask import redirect, render_template, url_for
from flask.blueprints import Blueprint
from flask.typing import ResponseReturnValue

# No page should be rendered from this route
bp = Blueprint("root", __name__, url_prefix="/")


# Redirect to main
@bp.route("/", methods=["GET"])
def home() -> ResponseReturnValue:
    return redirect(url_for("root.main"))


@bp.route("/home", methods=["GET"])
def main() -> ResponseReturnValue:
    # return redirect(url_for("first.page"))
    return render_template("temp/temp.html")
