from account import Account

jhon = Account(id=0, log_dir="log")
jhon.update(100) # Credit money
jhon.update(-150) # Handle insufficient balance. The program should not crash here. Display a msg.
jhon.update(-50) # Debit money
print("Balance:", jhon.balance) # View balance
print(jhon) # Give a str representation of the object
