from account import Account

class Bank:
    def __init__(self, log_dir):
        self.accounts = {} # key, val == id, Object
        self.log_dir = log_dir

    def open_account(self, id):
        self.accounts[id] = Account(id=id, log_dir=self.log_dir)
    
    def credit(self, id, amount):
        self.accounts[id].update(amount)

    def debit(self, id, amount):
        new_balance = self.accounts[id].balance - amount
        if new_balance < 0:
            print("Insufficient balance")
            return
        self.accounts[id].update(-amount)
    
    def transaction(self, sender_id, receiver_id, amount):
        # check sender's balance
        new_balance = self.accounts[sender_id].balance - amount
        if new_balance < 0:
            print("Insufficient balance")
            return
        self.debit(id=sender_id, amount=amount)
        self.credit(id=receiver_id, amount=amount)

    def get_ministatement(self, id):
        self.accounts[id].get_ministatement()
    
    def __str__(self):
        return f"Members: {len(self.accounts)} | Cash: {sum((acc.balance for acc in self.accounts.values()))}"
