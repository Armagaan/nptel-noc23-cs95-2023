import datetime
from read_last_n_lines import read_last_n_lines

class Account:
    def __init__(self, id, log_dir):
        self.id = id
        self.balance = 0
        self.logfile = f"{log_dir}/{id}.log"
        with open(self.logfile, "w") as file:
            pass

    def update(self, amount):
        new_balance = self.balance + amount
        if new_balance < 0:
            print("Insufficient balance")
            return
        self.balance = new_balance
        self._update_log(amount)

    def _update_log(self, amount):
        with open(self.logfile, "a") as file:
            file.write(f"{datetime.datetime.utcnow()} | {amount}\n")

    def get_ministatement(self):
        print(f"----- Ministatement id {self.id} -----")
        # transactions = read_last_n_lines(self.logfile)
        # with open(self.logfile, "r") as file:
        #     transactions = file.readlines()[-5:]

        transactions = read_last_n_lines(self.logfile, 5)
        for i, t in enumerate(transactions):
            print(i, t.strip())

    def __str__(self):
        return f"id : {self.id} | balance: {self.balance}"
