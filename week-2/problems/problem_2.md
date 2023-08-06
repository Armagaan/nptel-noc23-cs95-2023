# Problem 2: Match Braces

Write a function `matched(my_string)` that takes as input a string `my_string` and checks if the brackets `(` and `)` in `my_string` are matched: that is, every `(` has a matching `)` after it and every `)` has a matching `(` before it. Your function should ignore all other symbols that appear in `my_string`. Your function should return `True` if `my_string` has matched brackets and `False` if it does not.

Here are some examples to show how your function should work.

```python
>>> matched("zb%78")
True

>>> matched("(7)(a")
False

>>> matched("a)*(?")
False

>>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
True
```