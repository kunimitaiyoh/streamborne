from typing import Callable, Generic, TypeVar

T = TypeVar('T')

class Option(Generic[T]):
    def __init__(self, payload: T) -> None:
        self.payload = payload

    @property
    def is_present(self) -> bool:
        return self.payload is not None
