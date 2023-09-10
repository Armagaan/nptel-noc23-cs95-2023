from bank import Bank

bank = Bank(log_dir="log")

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
