from functools import cache

from flask import render_template
from flask.blueprints import Blueprint
from flask.typing import ResponseReturnValue

from webapp.handler.azure import doc_hist_get

# No page should be rendered from this route
bp = Blueprint("history", __name__, url_prefix="/history")


@cache
def get_select() -> list[str]:
    return [
        "timestamp",
        "filename",
        "fileIndex",
        "fileLength",
        "invoiceId",
        "invoiceDate",
        "dueDate",
        "customerId",
        "customerName",
        "invoiceTotal",
        "amountDue",
    ]


# Redirect to main
@bp.route("/", methods=["GET"])
def home() -> ResponseReturnValue:
    return render_template("history/history.html")


@bp.route("/form", methods=["POST"])
def form() -> ResponseReturnValue:
    select = get_select()
    table = doc_hist_get(select)

    return render_template(
        "history/table.html",
        table=table,
    )
