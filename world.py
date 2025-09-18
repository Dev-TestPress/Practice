# ---------------------------
# ATM Simulation in Python
# ---------------------------

class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def show_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect old PIN!")

# ---------------------------
# Main Program
# ---------------------------

atm = ATM(pin="1234", balance=10000)

print("Welcome to Python ATM!")
for attempt in range(3):
    entered_pin = input("Enter your 4-digit PIN: ")
    if atm.check_pin(entered_pin):
        break
    else:
        print("Incorrect PIN. Try again.")
else:
    print("Too many incorrect attempts. Exiting.")
    exit()

while True:
    print("\nSelect an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        atm.show_balance()
    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        atm.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))
        atm.withdraw(amount)
    elif choice == "4":
        old_pin = input("Enter old PIN: ")
        new_pin = input("Enter new PIN: ")
        atm.change_pin(old_pin, new_pin)
    elif choice == "5":
        print("Thank you for using Python ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1-5.")





