import atexit
import re
from contextlib import suppress
from datetime import date
from enum import StrEnum, unique
from http import HTTPStatus
from logging import Logger
from typing import TYPE_CHECKING, Any

from dotenv import dotenv_values
from flask import Flask, current_app
from werkzeug.serving import WSGIRequestHandler, is_running_from_reloader

from webapp.config import FlaskManager, filters, loading
from webapp.handler.logger import set_file, set_logger, set_stream
from webapp.page import api, root

if TYPE_CHECKING:
    from flask.blueprints import Blueprint


@unique
class Logging(StrEnum):
    INIT = "#### Program initializing. ####"
    EXIT = "#### Program exiting. ####"


# Jinja template common variables
def inject_var() -> dict[str, Any]:
    return {
        "debug": current_app.debug,
        "jinja_year": date.today().year,
        "jinja_site": current_app.config.get("JINJA_SITE"),
        "jinja_htmx": current_app.config.get("JINJA_HTMX"),
        "jinja_mui": current_app.config.get("JINJA_MUI"),
    }


# Disable logging for selected endpoints
def _hide_endpt_logs(patterns: list[str]) -> None:
    _log_request = WSGIRequestHandler.log_request
    status = {HTTPStatus.OK, HTTPStatus.NOT_MODIFIED}
    pats = f"^(?:{'|'.join(patterns)})$"

    def match_pats(req: WSGIRequestHandler) -> re.Match[str] | None:
        with suppress(re.error, AttributeError):
            return re.match(pats, req.path)

    def log_request(self: WSGIRequestHandler, *args: int | str, **kwargs: int | str) -> None:
        if not (args[0] in status and match_pats(self)):
            _log_request(self, *args, **kwargs)

    WSGIRequestHandler.log_request = log_request


# Webapp initialization
def _initialize(log: Logger, app: Flask) -> dict[str, Any]:
    log.warning(Logging.INIT)
    args: dict[str, Any] = {}

    if dotenv := app.config.get("DOTENV"):
        app.config.update(dotenv_values(dotenv))

    # Global Objects, cam be reassign and modify
    with FlaskManager() as manager:  # noqa: F841
        pass

    if not app.debug:
        # Cron Jobs
        pass

    return args


# Webapp finalization
def _finalize(log: Logger, **args: Any) -> None:  # noqa: ARG001
    log.warning(Logging.EXIT)


# Webapp creation
def create_app(debug: bool = False, prod: bool = False) -> Flask:
    log = set_logger("handler", set_stream(), _file := set_file())
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_prefixed_env()
    app.config.from_object(loading(debug))
    app.context_processor(inject_var)

    if endpoints := app.config.get("FILTER_ENDPT"):
        _hide_endpt_logs(endpoints)

    # Apply logging settings
    # if some_log := app.config.get("SOME_LOG"):
    #     log.getChild("some").setLevel(some_log)
    app.logger.addHandler(_file)

    # Production settings
    if prod and log.hasHandlers():
        log.handlers[0].setLevel(1000)

    # For non debug mode and reloader process
    if not debug or is_running_from_reloader():
        args = _initialize(log, app)
        atexit.register(_finalize, log, **args)

    # Loading blueprints
    blueprints: list[Blueprint] = [api, root]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    # Jinja filtering template
    app.add_template_filter(zip, "zip")
    app.add_template_filter(filters.float2dt, "timestamp")

    return app
