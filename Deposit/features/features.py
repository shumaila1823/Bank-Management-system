class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Invalid or insufficient funds.")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_deposit=0.0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, name, initial_deposit)
            print("Account created successfully.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
        for acc in self.accounts.values():
            acc.display()
            print("-" * 30)


def main():
    bank = Bank()
    while True:
        print("\n=== Bank Management System ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw
