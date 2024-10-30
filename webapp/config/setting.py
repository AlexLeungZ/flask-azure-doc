from dataclasses import dataclass
from typing import ClassVar, Literal, TypeAlias

Log: TypeAlias = Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]


@dataclass
# Internal setting class
# Common Settings for Flask application
class _BaseSetting:
    # Flags for development and production
    DEBUG: ClassVar[bool] = False
    DEVELOPMENT: ClassVar[bool] = False

    # Environment variables
    DOTENV: str = ".env"

    # Logging level
    # SOME_LOG: Log = "WARNING"

    # Endpoint logging filters
    FILTER_ENDPT: ClassVar[list[str]] = [
        r"/static(/.+){2}\.map",
        r"/static(/.+){2}\.(ico|css|js)",
    ]

    # Jinja Variables
    JINJA_SITE: str = "Template"
    JINJA_HTMX: str = "2.0.2"
    JINJA_MUI: str = "5.0.6"


@dataclass
# Internal setting class
# Overrides for Production
class ProdSetting(_BaseSetting):
    pass


@dataclass
# Internal setting class
# Overrides for Development
class DevSetting(_BaseSetting):
    DEBUG: ClassVar[bool] = True
    DEVELOPMENT: ClassVar[bool] = True

    # Environment variables
    DOTENV: str = ".env.dev"


def loading(debug: bool) -> DevSetting | ProdSetting:
    return (DevSetting if debug else ProdSetting)()
