import datetime
import pytz
class Account:
    """Simple Account calss with balence"""

    def __init__(self,name,balance):
        self.name=name;
        self.balance = balance;
        self.transaction_list =[]
        print("Account created for "+self.name)

    def deposit(self,ammount):
        if ammount > 0:
            self.balance +=ammount
            self.transaction_list.append(pytz.utc.localize(datetime.datetime.utcnow()),ammount)
            self.show_balance()

    def withdraw(self,ammount):
        if 0 < ammount <= self.balance:
            self.balance -= ammount
        else:
            print("The ammount must be greater than zero")
        self.show_balance()

    def show_balance(self):
        print("balance is {}".format(self.balance))

    def show_transaction(self):
        for date, ammount in self.transaction_list:
            if ammount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                ammount *= -1
            print("{:6} on {} (local time was {})".format(ammount,tran_type,date,date.astimezone()))

if __name__== '__main__':
    tim = Account("Tim",0)
    tim.show_balance()
    tim.deposit(1000)
    tim.show_balance()
    tim.withdraw(500)
    tim.show_balance()

    tim.withdraw(3000)