import re
from contextlib import suppress
from datetime import datetime
from functools import cache


# Filter function
# Converting float to datetime object or None
def float2dt(time: float) -> datetime | None:
    with suppress(TypeError):
        return datetime.fromtimestamp(time)


@cache
def _titling_re() -> re.Pattern[str]:
    return re.compile(r"(?<=\w)([A-Z0-9])")


@cache
def titling(string: str) -> str:
    s = re.sub(_titling_re(), r" \1", string)
    return s.title()
