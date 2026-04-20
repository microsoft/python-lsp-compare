from typing import TypeVar

T = TypeVar("T")


def identity(value: T) -> T:
    return value


text = identity("hello")
