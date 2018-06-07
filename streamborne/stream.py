import itertools
from typing import Callable, Generic, Iterator, TypeVar

T = TypeVar('T')
U = TypeVar('U')

class Stream(Generic[T]):
    def __init__(self, data: Iterator[T]) -> None:
        self.data = data

    def map(self, func: Callable[[T], U]) -> Stream[U]:
        return Stream(map(func, self.data))
