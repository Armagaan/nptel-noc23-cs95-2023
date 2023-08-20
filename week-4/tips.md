# Tips

## Generators vs Lists
```python
>>> word = "Hello"

>>> (letter in word) # generator
<generator object <genexpr> at 0x000002104D101F20>

>>> [letter in word] # list
['h', 'e', 'l', 'l', 'o']
```

## List Comprehension
```python
word = "Hello"
vowels = ["a", "e", "i", "o", "u"]

>>> # Smaller list:
>>> [True for letter in word if letter in vowels]
[True, True]

>>> # A list of same length:
>>> [True if letter in vowels else False for letter in word]
[False, True, False, False, True]

>>> # Invalid syntax
>>> # If used after "for", only if should be used.
>>> [True for letter in word if letter in vowels else False]
SyntaxError: invalid syntax

>>> # Invalid syntax
>>> # If used before "for", both if and else must be used.
>>> [True if letter in vowels for letter in word]
SyntaxError: invalid syntax
```
