# Problem 1

We have a list of annual rainfall recordings of cities. Each element in the list is of the form `(c, r)` where `c` is the city and `r` is the annual rainfall for a particular year. The list may have multiple entries for the same city, corresponding to rainfall recordings in different years.

Write a Python function `rain_average(l)` that takes as input a list of rainfall recordings and computes the avarage rainfall for each city. The output should be a list of pairs `(c, avg_r)` where `c` is the city and `avg_r` is the average rainfall for this city among the recordings in the input list. Note that `avg_r` should be of type `float`. The output should be sorted in alphabetical order with respect to the city name.

Here are some examples to show how `rain_average(l)` should work:
```python
>>> rain_average([('Bombay', 848),('Madras', 103),('Bombay', 923),('Bangalore', 201),('Madras', 128)])

[('Bangalore', 201.0), ('Bombay', 885.5), ('Madras', 115.5)]


>>> rain_average([('Bombay', 1848), ('Bombay', 923), ('Bombay', 201), ('Bombay', 128), ('Bombay', 103), ('Bombay', 948), ('Bangalore', 323)])

[('Bangalore', 323.0), ('Bombay', 691.8333333333334)]
```