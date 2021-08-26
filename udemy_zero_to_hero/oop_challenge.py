class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return f'Deposit of {amount} accepted. Current balance is {self.balance}'
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Funds Unavailable!'
        else:
            self.balance = self.balance - amount
            return f'Withdraw of {amount} done. Current balance is {self.balance}'
        

account1 = Account('Jose', 100)
print(account1.deposit(100))
print(account1.withdraw(200))
