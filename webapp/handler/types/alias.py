from collections.abc import Callable, Mapping
from typing import Any, TypeAlias, TypeVar

TDict: TypeAlias = Mapping[str, Any]
TPipe: TypeAlias = Callable[[Any], Any]
TvDict = TypeVar("TvDict", bound=TDict)
TvAny = TypeVar("TvAny")
