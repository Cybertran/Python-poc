import sqlite3
db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS account(name TEXT PRIMARY KEY NOT NULL ,balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions(time TIMESTAMP NOT NULL ,account TEXT NOT NULL ,amount INTEGER NOT NULL ,PRIMARY KEY (time,account))")

class Account:
    """Simple Account calss with balence"""

    def __init__(self,name : str,opening_balance:int = 0 ):
        self.name = name;
        self._balance = opening_balance;
        print("Account created for "+self.name,end='')

    def deposit(self,amount: int) -> float:
        if amount > 0.0:
            self._balance += amount
            print("{:.2f} deposited".format(amount/100))
        return self._balance/100

    def withdraw(self,amount) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print("{:.2f} withdrown".format(amount/100))
            return amount/100
        else:
            print("The ammount must be greater than zero")
            return 0.0

    def show_balance(self):
        print("balance on the account{} is {:.2f}".format(self.name,self._balance/100))

    # def show_transaction(self):
    #     for date, ammount in self.transaction_list:
    #         if ammount > 0:
    #             tran_type = "deposited"
    #         else:
    #             tran_type = "withdrawn"
    #             ammount *= -1
    #         print("{:6} on {} (local time was {})".format(ammount,tran_type,date,date.astimezone()))

if __name__=='__main__':

  john = Account("john")
  john.deposit(1010)
  john.deposit(10)
  john.withdraw(5)
  john.show_balance()