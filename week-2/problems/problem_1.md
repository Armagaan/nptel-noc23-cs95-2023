# Problem 1: Prime Partition

A positive integer `m` can be partitioned as primes if it can be written as `p + q` where `p > 0, q > 0` and both `p` and `q` are prime numbers. <br>
Write a Python function `prime_partition(m)` that takes an integer `m` as input and returns `True` if `m` can be partitioned as primes and `False` otherwise. (If `m` is not positive, your function should return `False`.)

```python
>>> prime_partition(7)
True

>>> prime_partition(185)
False

>>> prime_partition(3432)
True
```