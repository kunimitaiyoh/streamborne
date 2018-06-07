import itertools
from typing import Callable, Generic, Iterator, List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

class Stream(Generic[T]):
    def __init__(self, data: Iterator[T]) -> None:
        self.data = data

    # region intermediate operations
    def map(self, func: Callable[[T], U]) -> 'Stream[U]':
        return Stream(map(func, self.data))

    # endregion
    # region terminal operation
    def as_list(self) -> List[T]:
        return list(self.data)
    # endregion
def from_list(data: Iterator[T]) -> Stream[T]:
    return Stream(data)
