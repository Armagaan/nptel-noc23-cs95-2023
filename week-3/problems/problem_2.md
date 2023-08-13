# Problem 2

A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix:
```
1  2  3
4  5  6 
7  8  9
```
would be represented as `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`.

A horizonatal flip reflects each row. For instance, if we flip the previous matrix horizontally, we get
```
3  2  1
6  5  4 
9  8  7
```
which would be represented as `[[3, 2, 1], [6, 5, 4], [9, 8, 7]]`.

A vertical flip reflects each column. For instance, if we flip the previous matrix that has already been flipped horizontally, we get:
```
7  8  9
4  5  6
1  2  3
```
which would be represented as `[[7, 8, 9], [4, 5, 6], [1, 2, 3]]`.

Write a Python function `flip_matrix(m,d)` that takes as input a two dimensional matrix m and a direction `d`, where `d` is either `'h'` or `'v'`. If `d == 'h'`, the function should return the matrix flipped horizontally. If `d == 'v'`, the function should retun the matrix flipped vertically. For any other value of `d`, the function should return `m` unchanged. In all cases, the argument `m` should remain undisturbed by the function.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

```python
>>> matrix = [[1, 2], [3, 4]]

>>> matrix # You'll be supplied a function to print a matrix row-wise.
[1, 2]
[3, 4]

>>> flip_matrix(matrix, 'h')
[2, 1]
[4, 3]

>>> matrix
[1, 2]
[3, 4]

>>> flip_matrix(matrix, 'v')
[3, 4]
[1, 2]

>>> matrix
[1, 2]
[3, 4]

>>> flip_matrix(flip_matrix(matrix, 'h'), 'v')
[4, 3]
[2, 1]

>>> matrix
[1, 2]
[3, 4]

>>> flip_matrix(flip_matrix(matrix, 'h'), 'v')
[4, 3]
[2, 1]

>>> matrix
[1, 2]
[3, 4]
```
