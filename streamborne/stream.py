import itertools
from typing import Callable, Generic, Iterator, List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

class Stream(Generic[T]):
    def __init__(self, data: Iterator[T]) -> None:
        self.data = data

    def map(self, func: Callable[[T], U]) -> 'Stream[U]':
        return Stream(map(func, self.data))

    def as_list(self) -> List[T]:
        return list(self.data)

def from_list(data: Iterator[T]) -> Stream[T]:
    return Stream(data)
