# Build a BankAccount class with:
# - __init__ with account_holder and balance
# - deposit() method
# - withdraw() method (with balance check)
# - __str__ method to display account info


class BankAccount:
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance
    

    def deposit(self, amount):
        if amount <= 0:
            print(f"There is no amount to be deposited")
        else:
            self.balance += amount
            print(f'The balance amount is {self.balance}')
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount to withdraw")
        
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            print(f'The remaining balance is {self.balance}')

    def __str__(self):
        return f"This account is handled by {self.acc_holder}, Their balance is {self.balance}"


if __name__ == "__main__":
    obj = BankAccount('Steve', 4500)
    print(str(obj))
    obj.deposit(500)
    obj.withdraw(500)
    obj.withdraw(6000)


# Output:
# python3 bankacc_class.py 
# This account is handled by Steve, Their balance is 4500
# The balance amount is 5000
# The remaining balance is 4500
# Insufficient funds
        

