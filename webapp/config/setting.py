from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import ClassVar, Literal, Self, TypeAlias

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
    DATABASE: str = "database"
    SCHEMA: str = "sqlite"

    HIST_DB: str = "history.db"
    HIST_SC: str = "history.sql"

    # Logging level
    # SOME_LOG: Log = "WARNING"

    # Endpoint logging filters
    FILTER_ENDPT: ClassVar[list[str]] = [
        r"/static(/.+){2}\.map",
        r"/static(/.+){2}\.(ico|css|js)",
    ]

    # Jinja Variables
    JINJA_SITE: str = "AlexLeungZ"
    JINJA_HTMX: str = "2.0.2"
    JINJA_MUI: str = "5.0.6"

    @cached_property
    def _db_dir(self: Self) -> Path:
        if not (path := Path(self.DATABASE)).is_dir():
            return Path.cwd().parent / self.DATABASE
        return path

    @cached_property
    def _sc_dir(self: Self) -> Path:
        return Path("webapp") / self.SCHEMA

    @cached_property
    def HIST_DIR_DB(self: Self) -> Path:
        return self._db_dir / self.HIST_DB

    @cached_property
    def HIST_DIR_SC(self: Self) -> Path:
        return self._sc_dir / self.HIST_SC


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
    DOTENV: str = ".env"


def loading(debug: bool) -> DevSetting | ProdSetting:
    return (DevSetting if debug else ProdSetting)()
