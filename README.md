# streamborne

[![Build Status](https://travis-ci.org/kunimitaiyoh/streamborne.svg)](https://travis-ci.org/kunimitaiyoh/streamborne)
[![codecov](https://codecov.io/gh/kunimitaiyoh/streamborne/branch/master/graph/badge.svg)](https://codecov.io/gh/kunimitaiyoh/streamborne)

Streamborne is a completely statically typed wrapper of built-in functions and itertools that provides a fluent API for data operations.

| group     | function                        | supported |
|-----------|---------------------------------|-----------|
| built-in  | `abs`                           | no        |
| built-in  | `all`                           | not yet   |
| built-in  | `any`                           | not yet   |
| built-in  | `ascii`                         | no        |
| built-in  | `bin`                           | no        |
| built-in  | `bool`                          | no        |
| built-in  | `bytearray`                     | no        |
| built-in  | `bytes`                         | no        |
| built-in  | `callable`                      | no        |
| built-in  | `chr`                           | no        |
| built-in  | `classmethod`                   | no        |
| built-in  | `compile`                       | no        |
| built-in  | `complex`                       | no        |
| built-in  | `delattr`                       | no        |
| built-in  | `dict`                          | not yet   |
| built-in  | `dir`                           | no        |
| built-in  | `divmod`                        | no        |
| built-in  | `enumerate`                     |           |
| built-in  | `eval`                          | no        |
| built-in  | `exec`                          | no        |
| built-in  | `filter`                        | not yet   |
| built-in  | `float`                         | no        |
| built-in  | `format`                        | no        |
| built-in  | `frozenset`                     |           |
| built-in  | `getattr`                       | no        |
| built-in  | `globals`                       | no        |
| built-in  | `hasattr`                       | no        |
| built-in  | `hash`                          | no        |
| built-in  | `help`                          | no        |
| built-in  | `hex`                           | no        |
| built-in  | `id`                            | no        |
| built-in  | `input`                         | no        |
| built-in  | `int`                           | no        |
| built-in  | `isinstance`                    | no        |
| built-in  | `issubclass`                    | no        |
| built-in  | `iter`                          |           |
| built-in  | `len`                           | not yet   |
| built-in  | `list`                          | not yet   |
| built-in  | `locals`                        | no        |
| built-in  | `map`                           | not yet   |
| built-in  | `max`                           | not yet   |
| built-in  | `memoryview`                    | no        |
| built-in  | `min`                           | not yet   |
| built-in  | `next`                          |           |
| built-in  | `object`                        | no        |
| built-in  | `oct`                           | no        |
| built-in  | `open`                          | no        |
| built-in  | `ord`                           |           |
| built-in  | `pow`                           | no        |
| built-in  | `print`                         | no        |
| built-in  | `property`                      | no        |
| built-in  | `range`                         | no        |
| built-in  | `repr`                          | no        |
| built-in  | `reversed`                      | not yet   |
| built-in  | `round`                         |           |
| built-in  | `set`                           | not yet   |
| built-in  | `setattr`                       | no        |
| built-in  | `slice`                         | no        |
| built-in  | `sorted`                        | not yet   |
| built-in  | `staticmethod`                  | no        |
| built-in  | `str`                           | no        |
| built-in  | `sum`                           | not yet   |
| built-in  | `super`                         | no        |
| built-in  | `tuple`                         | no        |
| built-in  | `type`                          | no        |
| built-in  | `vars`                          | no        |
| built-in  | `zip`                           | not yet   |
| itertools | `count`                         |           |
| itertools | `cycle`                         | not yet   |
| itertools | `repeat`                        |           |
| itertools | `accumulate`                    | not yet   |
| itertools | `chain`                         | not yet   |
| itertools | `chain.from_iterable`           |           |
| itertools | `compress`                      |           |
| itertools | `dropwhile`                     | not yet   |
| itertools | `filterfalse`                   | not yet   |
| itertools | `groupby`                       | not yet   |
| itertools | `islice`                        | not yet   |
| itertools | `starmap`                       | not yet   |
| itertools | `takewhile`                     | not yet   |
| itertools | `tee`                           | not yet   |
| itertools | `zip_longest`                   | not yet   |
| itertools | `product`                       |           |
| itertools | `permutations`                  |           |
| itertools | `combinations`                  |           |
| itertools | `combinations_with_replacement` |           |
