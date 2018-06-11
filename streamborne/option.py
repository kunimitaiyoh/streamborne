from typing import Callable, Generic, Optional, TypeVar, Union
from streamborne.stream import Stream

T = TypeVar('T')
U = TypeVar('U')
E = TypeVar('E', bound=BaseException)

class Option(Generic[T]):
    def __init__(self, payload: T) -> None:
        self.payload = payload

    def get(self) -> T:
        raise NotImplementedError

    def is_present(self) -> bool:
        return self.payload is not None

    def is_empty(self) -> bool:
        return self.payload is not None

    def if_present(self, action: Callable[[T], None]) -> None:
        raise NotImplementedError

    def filter(self, predicate: Callable[[T], bool]) -> 'Option[T]':
        raise NotImplementedError

    def map(self, mapper: Callable[[T], U])-> 'Option[U]':
        raise NotImplementedError

    def flat_map(self, mapper: Callable[[T], 'Option[U]']) -> 'Option[T]':
        raise NotImplementedError

    def or_else(self, other: T) -> T:
        raise NotImplementedError

    def or_else_get(self, supplier: Callable[[], T]) -> T:
        raise NotImplementedError

    def or_else_throw(self, exception_supplier: Callable[[], E]) -> T:
        raise NotImplementedError

    def or_none(self) -> 'Optional[T]':
        raise NotImplementedError

    def stream(self) -> 'Stream[T]':
        raise NotImplementedError

    @staticmethod
    def of(value: T) -> 'Option[T]':
        raise NotImplementedError

    @staticmethod
    def of_nullable(value: Optional[T]) -> 'Option[T]':
        raise NotImplementedError

    @staticmethod
    def empty() -> 'Option[T]':
        raise NotImplementedError
