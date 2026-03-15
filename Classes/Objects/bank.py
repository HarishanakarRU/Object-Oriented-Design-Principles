class BankAccount:
    '''
    Requirements:

    Design Bank Account Class

    Problem: Create a BankAccount class that manages a simple bank account with deposit, withdrawal, and balance checking functionality.

    Requirements:

    Fields: accountNumber, ownerName, balance
    Constructor that initializes the account with owner name and account number (balance starts at 0)
    deposit(amount): adds money to balance (only positive amounts)
    withdraw(amount): removes money if sufficient balance exists, returns success/failure
    getBalance(): returns current balance
    '''

    account_number = 0
    owner_name = ""
    balance = 0

    def __init__(self, account_number, owner_name):
        self.account_number = account_number
        self.owner_name = owner_name
    
    def deposit(self, amount):
        self.balance += amount
        return True
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
            return False
        self.balance -= amount
        return True

    def get_balance(self):
        print(f"You have ${self.balance} in your account")
        return self.balance

# Test Class

account = BankAccount("123456", "John Doe")
account.deposit(1000)
print(account.get_balance())  # Should print 1000.0

success = account.withdraw(500)
print(str(success).lower())   # Should print true
print(account.get_balance())  # Should print 500.0

success = account.withdraw(1000)
print(str(success).lower())   # Should print false
