class BankAccount:
    def __init__(self,account_balance = 0):
        self.account_balance = account_balance

    def deposit (self,amount):
       
        self.account_balance += amount
        return self.account_balance 
    

    def withdraw (self,amount): 
        if self.account_balance >= amount :
            self.account_balance -= amount 
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

    def __str__(self):
        return f"The current balance is ${self.account_balance}"
    
# account=BankAccount(100)
# account.deposit(50)
# account.withdraw(30)
# account.display_balance()
# print(account)
