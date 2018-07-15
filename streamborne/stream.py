from functools import reduce
import itertools
from typing import (
    Callable,
    Dict,
    Generic,
    Iterable,
    List,
    Optional,
    Reversible,
    TypeVar,
    Tuple,
    Set,
    Sized,
)
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
        return self.next(lambda xs: filter(predicate, xs))

    def filterfalse(self, predicate: Predicate) -> 'Stream[T]':
        return self.next(lambda xs: itertools.filterfalse(predicate, xs))

    def map(self, function: Mapper) -> 'Stream[U]':
        return self.next(lambda xs: map(function, xs))

    def takewhile(self, predicate: Predicate) -> 'Stream[T]':
        return self.next(lambda xs: itertools.takewhile(predicate, xs))

    def dropwhile(self, predicate: Predicate) -> 'Stream[T]':
        return self.next(lambda xs: itertools.dropwhile(predicate, xs))

    def reversed(self) -> 'Stream[T]':
        if isinstance(self.data, Reversible):
            return self.next(lambda xs: reversed(xs))
        else:
            raise TypeError()

    def sorted(self, key_selector: Optional[Mapper]=(lambda x: x), reverse: bool=False) -> 'Stream[T]':
        return self.next(lambda xs: sorted(xs, key=key_selector, reverse=reverse))

    def accumulate(self, function: Callable[[T, T], T]) -> 'Stream[T]':
        # FIXME: confused constraint by mypy (function: Callable[[T, U], U])
        return self.next(lambda xs: itertools.accumulate(xs, function))

    def chain(self, other: Iterable[T]) -> 'Stream[T]':
        return self.next(lambda xs: itertools.chain(xs, other))

    def chain_from_iterable(self, other: Iterable[Iterable[T]]) -> 'Stream[T]':
        return self.next(lambda xs: itertools.chain.from_iterable(other))

    def groupby(self, key_selector: Callable[[T], T]) -> 'Stream[Tuple[T, Iterable[T]]]':
        # FIXME: confused constraint by mypy (key_selector: Callable[[T, U], U])
        return self.next(lambda xs: itertools.groupby(xs, key_selector))

    def cycle(self) -> 'Stream[T]':
        return self.next(lambda xs: itertools.cycle(xs))

    def zip(self, items: Iterable[U]) -> 'Stream[Tuple[T, U]]':
        return self.next(lambda xs: zip(xs, items))

    # TODO: need to implement `start`-omitted one.
    def islice(self, start: int, stop: int) -> 'Stream[T]':
        return self.next(lambda xs: itertools.islice(xs, start, stop))
    # endregion
    # region terminal operations for aggregation
    def all(self) -> bool:
        return self.terminate(lambda xs: all(xs))

    def any(self) -> bool:
        return self.terminate(lambda xs: any(xs))

    def apply(self, function: Callable[[Iterable[T]], U]) -> U:
        return self.terminate(lambda xs: function(xs))

    def len(self) -> int:
        if isinstance(self.data, Sized):
            return self.terminate(len)
        else:
            raise TypeError()

    def max(self) -> T:
        return self.terminate(lambda xs: max(xs))

    def reduce(self, function: Callable[[U, T], U], initial: U) -> U:
        return self.terminate(lambda xs: reduce(function, xs, initial))

    # type of 'start'? 🤔
    def sum(self, start: T) -> T:
        if start is not None:
            return self.terminate(lambda xs: sum(xs, start))
        else:
            return self.terminate(lambda xs: sum(xs))

    def tee(self) -> Tuple['Stream[T]', 'Stream[T]']:
        def f(xs: Iterable[T]) -> Tuple['Stream[T]', 'Stream[T]']:
            a, b = itertools.tee(xs)
            return (Stream(a), Stream(b))
        return self.terminate(f)
    # endregion
    # region terminal operations for collecting
    def dict(self, key_selector: Callable[[T], K], value_selector: Mapper) -> Dict[K, U]:
        return (
            self.map(lambda xs: (key_selector(xs), value_selector(xs)))
                .terminate(dict)
        )

    def list(self) -> List[T]:
        return self.terminate(list)

    def set(self) -> Set[T] :
        return self.terminate(set)
    # endregion
    # region private functions
    def next(self, next_function: Callable[[Iterable[T]], Iterable[U]]) -> 'Stream[U]':
        if (self.closed):
            raise IOError
        else:
            self.closed = True
            return Stream(next_function(self.data))

    def terminate(self, terminate: Callable[[Iterable[T]], U]) -> U:
        if (self.closed):
            raise IOError
        else:
            self.closed = True
            return terminate(self.data)
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
