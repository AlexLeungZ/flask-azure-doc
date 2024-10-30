from ast import literal_eval
from collections.abc import Callable, Iterable
from contextlib import suppress
from functools import cache
from inspect import get_annotations
from typing import Any, cast

from webapp.handler.types.alias import TDict, TPipe, TvAny, TvDict


# Internal functions
# Callable for no operation
def noop(var: TvAny) -> TvAny:
    return var


@cache
# Type manipulating functions
# Getting typed dict keys from target
def cached_annotations(target: Callable[..., object] | type[Any]) -> dict[str, Any]:
    return get_annotations(target)


# Type manipulating functions
# Trimming dict keys from object with init dict and cast as target
def trim_key(init: TvDict, obj: TDict, func: TPipe = noop) -> TvDict:
    return cast(TvDict, {key: func(obj[key]) if key in obj else init[key] for key in init})


# Type manipulating functions
# ast.literal_eval or original value
def eval_vals(val: Any) -> Any:
    with suppress(ValueError, SyntaxError):
        return literal_eval(val)
    return val


# Type manipulating functions
# ast.literal_eval for list
def eval_list(val: Iterable[Any]) -> list[Any]:
    return [eval_vals(elem) for elem in val]
