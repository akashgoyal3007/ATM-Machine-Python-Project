import datetime

class ATM:
    def __init__(self, pin):
        self.balance = 0
        self.pin = pin
        self.transaction_history = []

    def check_pin(self, input_pin):
        return self.pin == input_pin

    def change_pin(self, old_pin, new_pin):
        if self.check_pin(old_pin):
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Invalid current PIN.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount} on {datetime.datetime.now()}")
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount} on {datetime.datetime.now()}")
            print(f"${amount} withdrawn successfully.")
        else:
            print("Invalid or insufficient amount for withdrawal.")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def show_transaction_history(self):
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions available.")

def main():
    atm = ATM(pin=1234)  # Default PIN for demonstration purposes
    while True:
        print("\nWelcome to the ATM")
        print("1. Balance Inquiry")
        print("2. Cash Deposit")
        print("3. Cash Withdrawal")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = int(input("Please select an option: "))
        
        if choice == 1:
            input_pin = int(input("Enter your PIN: "))
            if atm.check_pin(input_pin):
                atm.check_balance()
            else:
                print("Invalid PIN.")
        
        elif choice == 2:
            input_pin = int(input("Enter your PIN: "))
            if atm.check_pin(input_pin):
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            else:
                print("Invalid PIN.")
        
        elif choice == 3:
            input_pin = int(input("Enter your PIN: "))
            if atm.check_pin(input_pin):
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            else:
                print("Invalid PIN.")
        
        elif choice == 4:
            old_pin = int(input("Enter your current PIN: "))
            new_pin = int(input("Enter your new PIN: "))
            atm.change_pin(old_pin, new_pin)
        
        elif choice == 5:
            input_pin = int(input("Enter your PIN: "))
            if atm.check_pin(input_pin):
                atm.show_transaction_history()
            else:
                print("Invalid PIN.")
        
        elif choice == 6:
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
