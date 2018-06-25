import functools
import itertools
from typing import Callable, Dict, Generic, Iterable, Optional, List, TypeVar, Tuple, Set
from streamborne.option import Option

T = TypeVar('T') # type of a Stream contains
U = TypeVar('U') # converted type from T
K = TypeVar('K') # type of a key for dicts

class Stream(Generic[T]):
    def __init__(self, data: Iterable[T]) -> None:
        self.data = data
        self.closed = False

    # region intermediate operations
    def filter(self, predicate: Callable[[T], bool]) -> 'Stream[T]':
        return self.next(lambda: filter(predicate, self.data))

    def map(self, func: Callable[[T], U]) -> 'Stream[U]':
        return self.next(lambda: map(func, self.data))

    def reversed(self) -> 'Stream[T]':
        raise NotImplementedError

    def sorted(self, key_selector: Optional[Callable[[T], U]]=None, reverse: bool=False) -> 'Stream[T]':
        raise NotImplementedError

    def zip(self, items: Iterable[U]) -> 'Stream[Tuple[T, U]]':
        raise NotImplementedError
    # endregion
    # region terminal operations for aggregation
    def all(self) -> bool:
        raise NotImplementedError

    def any(self) -> bool:
        raise NotImplementedError

    def len(self) -> int:
        raise NotImplementedError

    def max(self) -> T:
        raise NotImplementedError

    def reduce(self, function: Callable[[U, T], U], initial: U) -> U:
        raise NotImplementedError

    def set(self) -> Set[T] :
        raise NotImplementedError
    # type of 'start'? 🤔
    def sum(self, start: Optional[T]=None) -> T:
        raise NotImplementedError
    # endregion
    # region terminal operations for collecting
    def dict(self, key_selector: Callable[[T], K], value_selector: Callable[[T], U]) -> Dict[K, U]:
        raise NotImplementedError

    def list(self) -> List[T]:
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
    # region factory methods
    @staticmethod
    def from_list(data: Iterable[T]) -> 'Stream[T]':
        return Stream(data)

    @staticmethod
    def from_option(option: Option[T]) -> 'Stream[T]':
        item = option.map(lambda x: [x]).or_else_get(lambda: [])
        return Stream(item)
    # endregion
