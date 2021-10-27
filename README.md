# Roman / Arabic Numeral Conversion

```
from roman_numeral import to_arabic_numeral
>>> to_arabic_numeral("VI")
6
>>> to_arabic_numeral("IX")
9
# Bars are represented with a preceding pipe
>>> to_arabic_numeral("|V")
5000
>>> to_arabic_numeral("|IX")
9000
```


```
from roman_numeral import to_roman_numeral
>>> to_roman_numeral(6)
"VI"
>>> to_roman_numeral(9)
"IX"
# Bars are represented with a preceding pipe
>>> to_roman_numeral(5000)
"|V"
>>> to_roman_numeral(9000)
"|IX"
```
