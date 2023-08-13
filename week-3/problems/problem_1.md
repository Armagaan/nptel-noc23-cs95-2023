# Problem 1

Write a Python function `split_sum(l)` that takes a nonempty list of integers and returns a list `[pos, neg]`, where `pos` is the sum of squares all the positive numbers in `l` and `neg` is the sum of cubes of all the negative numbers in `l`.

Here are some examples to show how your function should work.

```python
>>> split_sum([1, 3, -5])
[10, -125]

>>> split_sum([2, 4, 6])
[56, 0]

>>> split_sum([-19, -7, -6, 0])
[0, -7418]

>>> split_sum([-1, 2, 3, -7])
[13, -344]
```
