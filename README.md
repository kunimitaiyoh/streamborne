# Streamborne

[![Build Status](https://travis-ci.org/kunimitaiyoh/streamborne.svg)](https://travis-ci.org/kunimitaiyoh/streamborne)
[![codecov](https://codecov.io/gh/kunimitaiyoh/streamborne/branch/master/graph/badge.svg)](https://codecov.io/gh/kunimitaiyoh/streamborne)

Streamborne is a completely statically typed wrapper of built-in functions and itertools that provides a fluent API for data operations.

| group     | function                        | supported |
|-----------|---------------------------------|-----------|
| built-in  | `all`                           | not yet   |
| built-in  | `any`                           | not yet   |
| built-in  | `dict`                          | not yet   |
| built-in  | `enumerate`                     | pending   |
| built-in  | `filter`                        | not yet   |
| built-in  | `frozenset`                     | pending   |
| built-in  | `iter`                          | pending   |
| built-in  | `len`                           | not yet   |
| built-in  | `list`                          | not yet   |
| built-in  | `map`                           | not yet   |
| built-in  | `max`                           | not yet   |
| built-in  | `min`                           | not yet   |
| built-in  | `next`                          | pending   |
| built-in  | `ord`                           | pending   |
| built-in  | `reversed`                      | not yet   |
| built-in  | `set`                           | not yet   |
| built-in  | `sorted`                        | not yet   |
| built-in  | `sum`                           | not yet   |
| built-in  | `zip`                           | not yet   |
| itertools | `count`                         | pending   |
| itertools | `cycle`                         | not yet   |
| itertools | `repeat`                        | pending   |
| itertools | `accumulate`                    | not yet   |
| itertools | `chain`                         | not yet   |
| itertools | `chain.from_iterable`           | pending   |
| itertools | `compress`                      | pending   |
| itertools | `dropwhile`                     | not yet   |
| itertools | `filterfalse`                   | not yet   |
| itertools | `groupby`                       | not yet   |
| itertools | `islice`                        | not yet   |
| itertools | `starmap`                       | not yet   |
| itertools | `takewhile`                     | not yet   |
| itertools | `tee`                           | not yet   |
| itertools | `zip_longest`                   | not yet   |
| itertools | `product`                       | pending   |
| itertools | `permutations`                  | pending   |
| itertools | `combinations`                  | pending   |
| itertools | `combinations_with_replacement` | pending   |

Streamborne does not support built-in functions as follows:  
`abs`, `ascii`, `bin`, `bool`, `bytearray`, `bytes`, `callable`, `chr`, `classmethod`, `compile`, `complex`, `delattr`, `dir`, `divmod`, `eval`, `exec`, `float`, `format`, `getattr`, `globals`, `hasattr`, `hash`, `help`, `hex`, `id`, `input`, `int`, `isinstance`, `issubclass`, `locals`, `memoryview`, `object`, `oct`, `open`, `pow`, `print`, `property`, `range`, `repr`, `round`, `setattr`, `slice`, `staticmethod`, `str`, `super`, `tuple`, `type`, `vars`.
