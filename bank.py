class Account:
    def __init__(self,accname,accountno,pin,old_balance,balance):
        self.accname = accname
        self.accountno = accountno
        self.pin = pin
        self.old_balance = old_balance
        self.balance = balance

    def  deposit(self):
         self.old_balance+=self.balance
         return f"Hello {self.accname}, your deposit is {self.old_balance}"
    def withdraw(self):
        self.old_balance-=self.balance
        return f"Hello {self.accname}, your withdrawal is {self.old_balance}"