class Account:
    def __init__(self,accname,accountno):
        self.accname = accname
        self.accountno = accountno
        self.balance = 0
    def  deposit(self,amount):
         if amount <=0:
             return f"Deposit must be positive amount"
         else:
             self.balance+=amount    
             return f"Hello {self.accname}, your deposit is {amount} and your new balance is {self.balance}"
    def withdraw(self,amount):
        if amount <=0:
            return f"Withdrawal amount must be greater than 0"
        elif amount > self.balance:
            return f"Hello {self.accname}, your balance is {self.balance} you can't withdraw {amount}"    
        else:    
            self.balance-=amount
            return f"Hello {self.accname}, your withdrawal is {amount} and your new balance is {self.balance}"