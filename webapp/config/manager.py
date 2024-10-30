from dataclasses import dataclass, field
from multiprocessing.managers import BaseManager

from apscheduler.schedulers.base import BaseScheduler


@dataclass
class _global:
    # Object can be reassigned here
    scheduler: BaseScheduler = field(init=False)


# Attributes as Global Variable
# Attributes are non-reassignable, but sub attributes can be reassigned
class FlaskManager(BaseManager):
    gvar: _global = _global()
