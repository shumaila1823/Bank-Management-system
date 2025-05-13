class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return False
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}")
        return True

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")

# Example usage:
if __name__ == "__main__":
    # Creating a sample account
    account = BankAccount("123456789", "Alice Smith", 1000.00)
    
    # Display initial info
    account.display_account_info()
    
    # Make a deposit
    amount_to_deposit = float(input("Enter amount to deposit: "))
    a
