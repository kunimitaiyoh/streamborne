import itertools
from typing import Callable, Generic, Iterable, List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

class Stream(Generic[T]):
    def __init__(self, data: Iterable[T]) -> None:
        self.data = data
        self.closed = False

    # region intermediate operations
    def map(self, func: Callable[[T], U]) -> 'Stream[U]':
        return self.next(lambda: map(func, self.data))

    # endregion
    # region terminal operation
    def as_list(self) -> List[T]:
        return self.terminate(lambda: list(self.data))
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
