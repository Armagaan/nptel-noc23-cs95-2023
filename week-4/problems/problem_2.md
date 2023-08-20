# Problem 2

A list in Python can contain nested lists. The degree of nesting need not be uniform. For instance `[1,2,[3,4,[5,6]]]` is a valid Python list. Write a Python function `flatten(l)` that takes a nonempty list of lists and returns a simple list of all the elements in the nested lists, flattened out.

You may use the following code which returns `True` if its input, `item`, is a list:
```python
isinstance(item, list)

item = 1
>>> isinstance(item, list)
False

item = [1]
>>> isinstance(item, list)
True
```

Here are some examples:
```python
>>> print(flatten([1, 2, [3], [4, [5, 6]]]))
[1, 2, 3, 4, 5, 6]

>>> print(flatten(["hello", True, 3]))
['hello', True, 3]

>>> print(flatten([[[]]]))
[]

>>> print(flatten([1, 2, 3, (4, 5, 6)]))
[1, 2, 3, (4, 5, 6)]

>>> print(flatten([1, 2, [3, ["hello", True]], [4, [5, 6]]]))
[1, 2, 3, 'hello', True, 4, 5, 6]
```
