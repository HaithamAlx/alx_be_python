class BankAccount:
    def __init__ (self, account_balance = None):
        if account_balance is not None:
            if float(self.read_from_file()) == account_balance:    
                self.account_balance = account_balance
            else:
                self.account_balance = float(self.read_from_file())
        else:
            pass

    def add_to_file(self):
        with open(r"C:\Users\einkw\Documents\Git\python\programming_paradigm_01\balance.txt",'w') as file:
            file.write(str(self.account_balance))

    def read_from_file(self):
            with open(r"C:\Users\einkw\Documents\Git\python\programming_paradigm_01\balance.txt",'r') as file:
                content = file.read()
                if content:
                    return content
                else:
                    pass
        
    def deposit(self, amount):
        self.account_balance = (float(self.read_from_file()))+amount
        self.add_to_file()

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance = (float(self.read_from_file()))-amount
            self.add_to_file()
            return True
        else:
            return False
        

    def display_balance(self):
        print(f'Current Balance: ${self.account_balance}')
