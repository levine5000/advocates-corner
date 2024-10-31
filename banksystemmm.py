class BankAccount:
    def __init__(self, account_holder, account_number , balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawal ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        print(f"{self.account_holder}, your balance is: ${self.balance}")

def main():
    print("Welcome to Bank System!")
    name=input("Enter your name to create an account: ")
    account = BankAccount(name, 1234567)

    while True:
        print("\nPlease choose an action:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice=input("Enter the number of your choice: ")
        if choice=="1":
            account.check_balance()
        elif choice=="2":
            amount=float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice=="3":
            amount=float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice=="4":
            print("Thank you for using the Bank System!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
