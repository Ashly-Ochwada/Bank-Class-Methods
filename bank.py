class Account:
    def __init__(self,accname,accountno):
        self.accname = accname
        self.accountno = accountno
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.transaction = 100
        
    def  deposit(self,amount):
        if amount <=0:
             return f"Deposit must be positive amount"
        else:
             self.balance+=amount   
             self.deposits.append(amount) 
             return f"Hello {self.accname}, your deposit is {amount} and your new balance is {self.balance} and your deposits are {self.deposits}" 
    def withdrawal(self,amount):
        if amount+self.transaction > self.balance:
            return f"Hello {self.accname}, your balance is {self.balance} you can't withdraw {amount}"    
        elif amount <=0:
            return f"Withdrawal amount must be greater than 0"
        else:    
            self.balance-=amount+self.transaction
            self.withdrawals.append(amount)
            return f"Hello {self.accname}, your withdrawal is {amount} and your new balance is {self.balance} and the withdrawals are {self.withdrawals}"
    def deposit_statements(self):
         for deposit in self.deposits:
             print(deposit, end="\n")
             
    def withdrawals_statement(self):
        for withdrawal in self.withdrawals:
            print(withdrawal,end="\n")

    def current_balance(self):
        return f"{self.balance}"        




   