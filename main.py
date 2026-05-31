from datetime import datetime

def log_transaction(username, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# strftime - formats to readable text string
    with open(f"logs/{username}.log", "a") as file:
        file.write(f"{timestamp} - {message}\n")

def update_balance(username, new_balance):
    lines = []

    with open("balances.txt", "r") as file:
        lines = file.readlines()

    with open("balances.txt", "w") as file:

        found = False

        for line in lines:
            name, balance = line.strip().split(",")

            if name == username:
                file.write(f"{username},{new_balance}\n")
                found = True
            else:
                file.write(line)

        if not found:
            file.write(f"{username},{new_balance}\n")

def get_balance(username):

    with open("balances.txt", "r") as file:

        for line in file:
            name, balance = line.strip().split(",")

            if name == username:
                return int(balance)

    return 0

class Account:

    def __init__(self, name):

        self.name = name
        self.balance = get_balance(name)

        log_transaction(name, "Account Accessed")

    def deposit(self, amount):

        self.balance += amount

        update_balance(self.name, self.balance)

        log_transaction(
            self.name,
            f"Deposited {amount}"
        )

    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient balance")

            log_transaction(
                self.name,
                f"Failed Withdrawal {amount}"
            )

            return

        self.balance -= amount

        update_balance(self.name, self.balance)

        log_transaction(
            self.name,
            f"Withdrawn {amount}"
        )

    def check_balance(self):
        print(f"Balance: {self.balance}")
    

a1 = Account("Ramesh")

a1.deposit(1000)
a1.withdraw(200)

#a1.check_balance()

a2 = Account("Suresh")

a2.deposit(900)
a2.withdraw(200)

#a2.check_balance()

a3 = Account("Mahi")
a3.deposit(10)
a3.withdraw(15)
a3.withdraw(6)
a3.check_balance()