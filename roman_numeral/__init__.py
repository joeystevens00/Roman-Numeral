from collections import OrderedDict
from functools import reduce
import operator
from typing import List, Union


class Bar(object):
    def __init__(self, base=1000):
        self.base = base

    def __add__(self, x: int) -> int:
        return self.base*x

    __radd__ = __add__


symbols = OrderedDict({
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    # When pipe precededs a character, consider it a bar over the next character
    '|':  Bar(),
})


def roman_symbol_floor(arabic_numeral: int) -> str:
    for roman_numeral, value in symbols.items():
        if type(value) == type(lambda: 0):
            continue
        remainder = arabic_numeral % value
        floor = arabic_numeral // value
        has_remainder = remainder > 0 and floor > 1 and floor < value
        if has_remainder or arabic_numeral == value:
            return roman_numeral


def symbol_values(roman_numeral: str) -> List[int]:
    return [
        symbols.get(c)
        for c in roman_numeral
    ]


def bar_values_in_place(values: List[Union[Bar, str]]) -> List:
    nvalues = []
    bar_active = False
    for index, v in enumerate(values):
        if isinstance(v, Bar):
            bar_active = True
        else:
            if bar_active:
                v = Bar()+v
                bar_active = False
            nvalues.append(v)
    return nvalues


def to_arabic_numeral(roman_numeral: str) -> int:
    values = symbol_values(roman_numeral)
    arabic_numeral_values = []
    bar_active = False
    for index, value in enumerate(values):
        if isinstance(value, Bar):
            bar_active = True
            continue
        future_values = bar_values_in_place(values[index:])
        is_largest = value >= max(future_values)
        if not is_largest:
            value = -value
        if bar_active:
            value = Bar() + value
            if is_largest:
                bar_active = False
        arabic_numeral_values.append(value)
    return reduce(operator.add, arabic_numeral_values)


# def to_roman_numeral(arabic_numeral: int) -> str:
