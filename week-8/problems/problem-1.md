# Problem 1

## 0/1 Knapsack

We are given `N` items, each having some weight and value associated with it, and a bag with capacity `W`, (i.e., the bag can hold at most `W` weight in it). We can only add an item once. The task is to put the items into the bag such that the sum of their values is maximum. Find the solution using dynamic programming.

Example:
```
N: 4
W: 8
Weights: (2, 3, 4, 5)
Values:  (1, 2, 5, 6)
--------------------
Profit: 8
Space used: 8
Itemset:
item:1, w:3, v:2
item:3, w:5, v:6
```
