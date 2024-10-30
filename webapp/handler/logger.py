from functools import cache
from logging import NOTSET, WARNING, Formatter, Handler, Logger, StreamHandler, getLogger
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import TextIO


@cache
# Logger settings
# Logger IO format
def _set_format() -> Formatter:
    return Formatter(
        "[%(asctime)s] %(levelname)s %(message)s",
        "%d/%b/%Y %H:%M:%S",
    )


@cache
# Logger settings
# Logger IO stream settings
def set_stream() -> StreamHandler[TextIO]:
    output = _set_format()
    stream = StreamHandler()
    stream.setLevel(NOTSET)
    stream.setFormatter(output)
    return stream


@cache
# Logger settings
# Logger file stream settings
def set_file() -> RotatingFileHandler:
    output = _set_format()
    path = Path("handler.log")  # Size: 8MB
    file = RotatingFileHandler(path, maxBytes=8388608, backupCount=3)
    file.setLevel(WARNING)
    file.setFormatter(output)
    return file


@cache
# Logger settings
# Default logger layout
def set_logger(name: str, stream: Handler, file: Handler) -> Logger:
    logger = getLogger(name)
    logger.addHandler(stream)
    logger.addHandler(file)
    logger.propagate = False
    return logger
