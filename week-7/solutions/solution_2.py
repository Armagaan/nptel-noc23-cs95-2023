from account import Account

jhon = Account(id=0, log_dir="log")
for i in range(1, 100):
    jhon.update(i)
jhon.get_ministatement()
