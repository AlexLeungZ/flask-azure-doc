from collections.abc import Callable
from contextlib import suppress
from datetime import datetime, timedelta
from functools import cache
from typing import Any, cast

from apscheduler.job import Job
from apscheduler.jobstores.base import JobLookupError
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
from apscheduler.triggers.date import DateTrigger

from webapp.config.manager import FlaskManager


@cache
# Cached timedelta function
# This function is called for all api requests
def delta(**kwargs: float) -> timedelta:
    return timedelta(**kwargs)


# Execute function at a specific time
# By removing and adding the job, as args is updated
def future(uuid: str, when: datetime, func: Callable[..., None], *args: Any) -> Job:
    with FlaskManager() as manager:
        skd = cast(Scheduler, manager.gvar.scheduler)
        trg = DateTrigger(when)

    with suppress(JobLookupError):
        skd.remove_job(uuid)
    return skd.add_job(func, trg, args, id=uuid)
