from dataclasses import dataclass
from multiprocessing.managers import BaseManager


@dataclass
class _global:
    # Object can be reassigned here
    pass


# Attributes as Global Variable
# Attributes are non-reassignable, but sub attributes can be reassigned
class FlaskManager(BaseManager):
    gvar: _global = _global()
