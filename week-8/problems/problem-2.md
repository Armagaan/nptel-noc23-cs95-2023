# Problem 2

## Unbounded Knapsack

We are given `N` items, each having some weight and value associated with it, and a bag with capacity `W`, (i.e., the bag can hold at most `W` weight in it). We can add an item as many times as possible. The task is to put the items into the bag such that the sum of their values is maximum. Find the solution using dynamic programming.

Example:
```
N: 4
W: 8
Weights: (2, 3, 4, 5)
Values:  (1, 2, 5, 6)
--------------------
Profit: 10
Space used: 8
Itemset:
item:2, w:4, v:5
item:2, w:4, v:5
```

value_without_item = dp[row-1][col]
value_with_item = val[row] + dp[row-1][col - weight[row]]
max(value_without, value_with)