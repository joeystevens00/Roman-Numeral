import pytest

import roman_numeral


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("I", 1),
        ("II", 2),
        ("III", 3),
        ("IV", 4),
        ("V", 5),
        ("VI", 6),
        ("VII", 7),
        ("VIII", 8),
        ("IX", 9),
        ("X", 10),
        ("XI", 11),
        ("XII", 12),
        ("XIII", 13),
        ("XIV", 14),
        ("XV", 15),
        ("XVI", 16),
        ("XVII", 17),
        ("XVIII", 18),
        ("XIX", 19),
        ("XX", 20),
        ("XXI", 21),
        ("XXII", 22),
        ("XXIII", 23),
        ("XXIV", 24),
        ("XXX", 30),
        ("XL", 40),
        ("L", 50),
        ("LX", 60),
        ("LXX", 70),
        ("LXXX", 80),
        ("XC", 90),
        ("C", 100),
        ("CI", 101),
        ("CII", 102),
        ("CC", 200),
        ("CCC", 300),
        ("CD", 400),
        ("D", 500),
        ("DC", 600),
        ("DCC", 700),
        ("DCCC", 800),
        ("CM", 900),
        ("M", 1000),
        ("MI", 1001),
        ("MII", 1002),
        ("MIII", 1003),
        ("MCM", 1900),
        ("MM", 2000),
        ("MMI", 2001),
        ("MMII", 2002),
        ("MMC", 2100),     # 1000 + 1000 + 100
        ("MMM", 3000),     # 1000 + 1000 + 1000
        ("M|V", 4000),     #-1000 + 5000
        ("|V", 5000),      # 1000 * 5
        ("|IX", 9000),     # 1000 * (-1 + 10)
        ("|M", 1_000_000), # 1000 * 1000
    ]
)
def test_to_arabic_numeral(test_input, expected):
    assert roman_numeral.to_arabic_numeral(test_input) == expected

#
# @pytest.mark.parametrize(
#     "test_input,expected",
#     [
#         (1, "I"),
#         (2, "II"),
#         (3, "III"),
#         (4, "IV"),
#         (5, "V"),
#         (6, "VI"),
#         (7, "VII"),
#         (8, "VIII"),
#         (9, "IX"),
#         (10, "X"),
#         (11, "XI"),
#         (12, "XII"),
#         (13, "XIII"),
#         (14, "XIV"),
#         (15, "XV"),
#         (16, "XVI"),
#         (17, "XVII"),
#         (18, "XVIII"),
#         (19, "XIX"),
#         (20, "XX"),
#         (21, "XXI"),
#         (22, "XXII"),
#         (23, "XXIII"),
#         (24, "XXIV"),
#         (30, "XXX"),
#         (40, "XL"),
#         (50, "L"),
#         (60, "LX"),
#         (70, "LXX"),
#         (80, "LXXX"),
#         (90, "XC"),
#         (100, "C"),
#         (101, "CI"),
#         (102, "CII"),
#         (200, "CC"),
#         (300, "CCC"),
#         (400, "CD"),
#         (500, "D"),
#         (600, "DC"),
#         (700, "DCC"),
#         (800, "DCCC"),
#         (900, "CM"),
#         (1000, "M"),
#         (1001, "MI"),
#         (1002, "MII"),
#         (1003, "MIII"),
#         (1900, "MCM"),
#         (2000, "MM"),
#         (2001, "MMI"),
#         (2002, "MMII"),
#         (2100, "MMC"),
#         (3000, "MMM"),
#         (4000, "M|V"),
#         (5000, "|V"),
#         (9000, "|IX")
#         (1_000_000, "|M"),
#     ]
# )
# def test_to_roman_numeral(test_input, expected):
#     assert roman_numeral.to_roman_numeral(test_input) == expected
