from flask import render_template, request
from flask.blueprints import Blueprint
from flask.typing import ResponseReturnValue

from webapp.config.manager import FlaskManager
from webapp.handler.azure import files2pipe

# No page should be rendered from this route
bp = Blueprint("loader", __name__, url_prefix="/loader")


# Redirect to main
@bp.route("/", methods=["GET"])
def home() -> ResponseReturnValue:
    ext = ".PDF,.JPEG,.JPG,PNG,BMP,TIFF,HEIF"

    return render_template(
        "loader/loader.html",
        ext=ext,
    )


@bp.route("/form", methods=["POST"])
def form() -> ResponseReturnValue:
    with FlaskManager() as manager:
        client = manager.gvar.client

    files = request.files.getlist("file")
    result = files2pipe(files, client)

    return render_template(
        "loader/table.html",
        result=result,
    )
