# PART 1: Custom Exceptions
# Create these custom exceptions:
# - InsufficientFundsError
# - InvalidAmountError
# - AccountNotFoundError

class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception): 
    pass

class AccountNotFoundError(Exception):
    pass

# PART 2: Rewrite BankAccount with proper error handling
# - Use your custom exceptions
# - Add type hints to ALL methods
# - Use try/except in the main block to catch errors gracefully

class BankAccount:
    withdraw_fee = 5
    def __init__(self, account_holder: str, balance:float) -> None:
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount:float) -> any:
        if amount <= 0:
            raise InvalidAmountError (f"Invalid amount: {amount}. Must be positive.")
        self.balance += amount
        print(f'Deposited :{amount}. Balance {self.balance}')
        
    
    def withdraw(self, amount:float) -> any:
        if amount<=0:
            raise InvalidAmountError (f"Invalid amount: {amount}. Must be positive.")
        if amount > (self.balance + self.withdraw_fee):
            raise InsufficientFundsError (f"The balance is less than amount to withdraw")
        self.balance -= amount
        print(f'Withdraw :{amount}. Balance {self.balance}')
    
    def __str__(self) -> str:
        return f"{self.account_holder}: ${self.balance}"

# Example with type hints:
# def deposit(self, amount: float) -> bool:

# PART 3: Create a Bank class that manages multiple accounts
# - add_account(account: BankAccount) -> None
# - get_account(account_holder: str) -> BankAccount (raise AccountNotFoundError if not found)
# - transfer(from_acc: str, to_acc: str, amount: float) -> bool


class Bank:
    def __init__(self) -> None:
        self.accounts= {}  # name -> account
    
    def add_account(self, account):
        self.accounts[account.account_holder] = account
        print(f"Account added: {account.account_holder}")
    
    def get_account(self, account_holder) :
        if account_holder not in self.accounts:
            raise AccountNotFoundError(f"Account '{account_holder}' not found")
        return self.accounts[account_holder]
    
    def transfer(self, from_name, to_name, amount) :
        from_acc = self.get_account(from_name)  # Raises if not found
        to_acc = self.get_account(to_name)      # Raises if not found
        from_acc.withdraw(amount)  # Raises if insufficient funds
        to_acc.deposit(amount)
        print(f"Transferred {amount} from {from_name} to {to_name}")
        return True

if __name__ == "__main__":
    bank = Bank()
    
    # Create accounts
    bank.add_account(BankAccount("Alice", 1000))
    bank.add_account(BankAccount("Bob", 500))
    
    # Test 1: Valid transfer
    try:
        bank.transfer("Alice", "Bob", 200)
    except (AccountNotFoundError, InsufficientFundsError, InvalidAmountError) as e:
        print(f"Transfer failed: {e}")
    
    # Test 2: Insufficient funds
    try:
        bank.transfer("Bob", "Alice", 10000)
    except InsufficientFundsError as e:
        print(f"Transfer failed: {e}")
    
    # Test 3: Account not found
    try:
        bank.transfer("Charlie", "Alice", 100)
    except AccountNotFoundError as e:
        print(f"Transfer failed: {e}")
    
    # Test 4: Invalid amount
    try:
        bank.get_account("Alice").deposit(-50)
    except InvalidAmountError as e:
        print(f"Deposit failed: {e}")
