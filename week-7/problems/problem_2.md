# Problem 2

Update your class `Account` so that it maintains a log of updates. Write a method that prints the ministatement. The ministatement contains the transaction time and amount of the 5 latest transactions and the balance.

Example:
```python
jhon = Account(id=0)
for i in range(1, 100):
    jhon.update(i)
jhon.get_ministatement()
```

Output:
```
----- Ministatement: id 0 -----
2023-09-10 11:27:08.114488+00:00 | 95
2023-09-10 11:27:08.114488+00:00 | 96
2023-09-10 11:27:08.114488+00:00 | 97
2023-09-10 11:27:08.114488+00:00 | 98
2023-09-10 11:27:08.115501+00:00 | 99
Balance: 4950
```
