import functools
import itertools
from typing import Callable, Dict, Generic, Iterable, Optional, List, TypeVar, Tuple, Set
from streamborne.option import Option

T = TypeVar('T') # type of a Stream contains
U = TypeVar('U') # converted type from T
K = TypeVar('K') # type of a key for dicts or grouping
Predicate = Callable[[T], bool]
Mapper = Callable[[T], U]

class Stream(Generic[T]):
    def __init__(self, data: Iterable[T]) -> None:
        self.data = data
        self.closed = False

    # region intermediate operations

    def filter(self, predicate: Predicate) -> 'Stream[T]':
        return self.next(lambda: filter(predicate, self.data))

    def filterfalse(self, predicate: Predicate) -> 'Stream[T]':
        raise NotImplementedError

    def map(self, function: Mapper) -> 'Stream[U]':
        return self.next(lambda: map(function, self.data))

    def takewhile(self, predicate: Predicate) -> 'Stream[T]':
        raise NotImplementedError

    def dropwhile(self, predicate: Predicate) -> 'Stream[T]':
        raise NotImplementedError

    def reversed(self) -> 'Stream[T]':
        raise NotImplementedError

    def sorted(self, key_selector: Optional[Mapper]=None, reverse: bool=False) -> 'Stream[T]':
        raise NotImplementedError

    def accumulate(self, function: Callable[[T, T], U]) -> 'Stream[U]':
        raise NotImplementedError

    def chain(self, other: Iterable[T]) -> 'Stream[T]':
        raise NotImplementedError

    def chain_from_iterable(self, other: Iterable[Iterable[T]]) -> 'Stream[T]':
        raise NotImplementedError

    def groupby(self, key_selector: Callable[[T], K]) -> 'Stream[T]':
        raise NotImplementedError

    def cycle(self) -> 'Stream[T]':
        raise NotImplementedError

    def zip(self, items: Iterable[U]) -> 'Stream[Tuple[T, U]]':
        raise NotImplementedError

    # TODO: need to implement `start`-omitted one.
    def islice(self, start: int, stop: int) -> 'Stream[T]':
        raise NotImplementedError

    def starmap(self, function: Callable[..., U]) -> 'Stream[U]':
        raise NotImplementedError


    def tee(self) -> Tuple['Stream[T]', 'Stream[T]']:
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
    def dict(self, key_selector: Callable[[T], K], value_selector: Mapper) -> Dict[K, U]:
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
