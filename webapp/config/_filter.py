from contextlib import suppress
from datetime import datetime


# Filter function
# Converting float to datetime object or None
def float2dt(time: float) -> datetime | None:
    with suppress(TypeError):
        return datetime.fromtimestamp(time)
