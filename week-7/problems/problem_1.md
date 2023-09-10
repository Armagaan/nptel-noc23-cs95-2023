# Problem 1

Write a class named `Account` for a bank account. It should support the following methods:

```python
jhon = Account(id=0)
jhon.update(100) # Credit money
jhon.update(-150) # Handle insufficient balance. The program should not crash here. Display a msg.
jhon.update(-50) # Debit money
print("Balance:", jhon.balance) # View balance
print("str rep:", jhon) # Give a str representation of the object
```

The output should look like this:
```python
Insufficient balance
Balance: 50
id: 0 | balance: 50
```
