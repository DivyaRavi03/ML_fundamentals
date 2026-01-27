# SavingsAccount that inherits from BankAccount
# - Has interest_rate attribute
# - Has apply_interest() method that adds interest to balance
# - Overrides withdraw() to charge $5 fee per withdrawal

import math 
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


class SavingsAccount(BankAccount):
    withdraw_fee = 5
    def __init__(self, acc_holder, balance, interest_rate):
        super().__init__(acc_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self, months):
        if self.balance <= 0 and months == 0:
            return self.balance
        if self.balance > 0:
            self.balance = self.balance * math.pow((1 + self.interest_rate/12), months) # Interest_rate = Principal * (1 + rate/n) ^ t * n
            return 'Your current balance after {} months is {}'.format(months, int(self.balance))
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount to withdraw")
        
        elif amount + self.withdraw_fee > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= (amount + self.withdraw_fee)
            print(f'The remaining balance is {self.balance} with after withdraw of ${amount} + fee ${self.withdraw_fee}')



if __name__ == "__main__":
    obj = BankAccount('Steve', 4500)
    print(str(obj))
    obj.deposit(500)
    obj.withdraw(500)
    obj.withdraw(6000)

    obj_2 = SavingsAccount('John', 6000, 0.08)
    print(obj_2)
    obj_2.withdraw(500)
    print(obj_2.apply_interest(24))
        
