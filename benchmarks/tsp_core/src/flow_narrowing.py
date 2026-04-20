from typing import Iterable


def handle(value: int | str | None) -> int:
    if isinstance(value, int):
        narrowed = value + 1
        return narrowed
    if value is None:
        return 0
    return len(value)
