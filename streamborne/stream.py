import functools
import itertools
from typing import Callable, Dict, Generic, Iterable, Optional, List, TypeVar

T = TypeVar('T') # type of a Stream contains
U = TypeVar('U') # converted type from T
K = TypeVar('K') # type of a key for dicts

class Stream(Generic[T]):
    def __init__(self, data: Iterable[T]) -> None:
        self.data = data
        self.closed = False

    # region intermediate operations
    def map(self, func: Callable[[T], U]) -> 'Stream[U]':
        return self.next(lambda: map(func, self.data))

    def filter(self, predicate: Callable[[T], bool]) -> 'Stream[T]':
        raise NotImplementedError
    # endregion
    # region terminal operations
    def reduce(self, function: Callable[[U, T], U], initial: U) -> U:
        raise NotImplementedError

    def as_list(self) -> List[T]:
        return self.terminate(lambda: list(self.data))

    def as_dict(self, key_selector: Callable[[T], K], value_selector: Callable[[T], U]) -> Dict[K, U]:
        raise NotImplementedError
    # endregion
    # region private functions
    def next(self, iterable_supplier: Callable[[], Iterable[U]]) -> 'Stream[U]':
        if (self.closed):
            raise IOError
        else:
            self.closed = True
            return Stream(iterable_supplier())

    def terminate(self, result_supplier: Callable[[], U]) -> U:
        if (self.closed):
            raise IOError
        else:
            self.closed = True
            return result_supplier()
    # endregion
def from_list(data: Iterable[T]) -> Stream[T]:
    return Stream(data)
