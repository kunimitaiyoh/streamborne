from typing import Callable, Generic, Optional, TYPE_CHECKING, TypeVar, Union

T = TypeVar('T')
U = TypeVar('U')
E = TypeVar('E', bound=BaseException)

if TYPE_CHECKING:
    from streamborne.stream import Stream

class Option(Generic[T]):
    def __init__(self, payload: Optional[T]) -> None:
        self.payload = payload

    def get(self) -> T:
        if (self.payload is not None):
            return self.payload
        else:
            raise TypeError('No value present.')

    def is_present(self) -> bool:
        return self.payload is not None

    def is_empty(self) -> bool:
        return self.payload is None

    def if_present(self, action: Callable[[T], None]) -> None:
        if self.is_present():
            action(self.get())

    def filter(self, predicate: Callable[[T], bool]) -> 'Option[T]':
        if self.is_present():
            return self if predicate(self.get()) else Option.empty()
        else:
            return self

    def map(self, mapper: Callable[[T], U])-> 'Option[U]':
        if self.is_present():
            return Option.of_nullable(mapper(self.get()))
        else:
            return Option.empty()

    def flat_map(self, mapper: Callable[[T], 'Option[U]']) -> 'Option[U]':
        if self.is_present():
            return mapper(self.get())
        else:
            return Option.empty()

    def or_else(self, other: T) -> T:
        if self.is_present():
            return self.get()
        else:
            return other

    def or_else_get(self, supplier: Callable[[], T]) -> T:
        if self.is_present():
            return self.get()
        else:
            return supplier()

    def or_else_throw(self, exception_supplier: Callable[[], E]) -> T:
        if self.is_present():
            return self.get()
        else:
            raise exception_supplier()

    def or_none(self) -> 'Optional[T]':
        return self.payload

    def stream(self) -> 'Stream[T]':
        from streamborne.stream import Stream
        return Stream.from_option(self)

    @staticmethod
    def of(value: T) -> 'Option[T]':
        if value is not None:
            return Option(value)
        else:
            raise TypeError

    @staticmethod
    def of_nullable(value: Optional[T]) -> 'Option[T]':
        if value is not None:
            return Option.of(value)
        else:
            return Option.empty()

    @staticmethod
    def empty() -> 'Option[T]':
        return Option(None)
