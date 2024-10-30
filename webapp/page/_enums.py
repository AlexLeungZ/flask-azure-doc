from enum import StrEnum, unique
from functools import cache
from typing import Self


@unique
# String Enum
# Meta class for logging messages
class LogNum(StrEnum):
    @cache
    def __str__(self: Self) -> str:
        return self.value

    @classmethod
    @cache
    def get(cls: type[Self], key: str | None) -> str | None:
        return cls[key].value if key and hasattr(cls, key) else key


# Logging Enum
# Message for page
# class PageLogBy(LogNum):
#     pass
