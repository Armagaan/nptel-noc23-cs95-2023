# Problem 3

Write a class for a bank. 

```python
bank = Bank()

# Open accounts
bank.open_account(id=0)
bank.open_account(id=1)

# Add balance.
bank.credit(0, 100)

# Transact
bank.transaction(sender_id=0, receiver_id=1, amount=10)

# View updates
print(bank)

print()
bank.get_ministatement(0)

# Debit
print()
bank.debit(1, 10)
bank.get_ministatement(1)

print()
print(bank)
```

Output
```
Members: 2 | Cash: 100

----- Ministatement: id 0 -----
2023-09-10 11:29:03.987089+00:00 | 100
2023-09-10 11:29:03.987089+00:00 | -10
Balance: 90

----- Ministatement: id 1 -----
2023-09-10 11:29:03.987089+00:00 | 10
2023-09-10 11:29:03.996338+00:00 | -10
Balance: 0

Members: 2 | Cash: 90
```