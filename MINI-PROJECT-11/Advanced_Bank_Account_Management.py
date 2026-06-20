class BankAccount:
    """Represents a simple banking system."""

    # Stores all account objects
    accounts = []

    # Stores transaction history
    history = {}

    def __init__(self,name,acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    @classmethod
    def add_account(cls,name,acc_no,balance):
        """Create and add a new bank account."""

        data = BankAccount(name,acc_no,balance)
        cls.accounts.append(data)

    @classmethod
    def deposit(cls,name,accno,amount):
        """Deposit money into an account."""

        found = False
        for account in cls.accounts:
            if account.name.lower() == name and account.acc_no == accno:
                found = True

                if amount <= 0:
                    print("Negative numbers can't be accepted!")

                else:
                    account.balance += amount

                    # Store deposit transaction
                    if account not in cls.history:
                        cls.history[account] = []
                        cls.history[account].append(f"{amount} deposited")

                        print(f"deposited {amount} from {account.acc_no}")
                        print(f"Current balance: {account.balance}")
                        break

        if not found:
            print("You entered username or acc_no wrong")

    @classmethod
    def withdraw(cls,name,accno,amount):
        """Withdraw money from an account."""

        found = False
        for account in cls.accounts:
            if account.name.lower() == name and account.acc_no == accno:
                found = True

                if account.balance >= amount and amount > 0:
                    account.balance -= amount

                    # Store withdrawal transaction
                    cls.history[account] = f"{amount} withdrawed"

                    print(f"Withdrawed {amount} from {account.acc_no}")
                    print(f"Current balance: {account.balance}")
                    break

                else:
                    print("Insufficient Balance! (or) may be you entered negative numbers")
                    break

        if not found:
            print("You entered username or acc_no wrong")

    @classmethod
    def show_accounts(cls):
        """Display all account details."""

        for account in cls.accounts:
            print(f"Name:{account.name}\nAccount no:{account.acc_no}\nBalance:{account.balance}")
            print()

    @classmethod
    def show_balance(cls,name,accno):
        """Display current account balance."""

        found = False
        for account in cls.accounts:
            if account.name.lower() == name and account.acc_no == accno:
                found = True
                print(f"Your current account balance: {account.balance}")
                break

        if not found:
            print("You entered username or acc_no wrong")


# Default account records
BankAccount.accounts = [
    BankAccount("Maneesh", 1001, 5000),
    BankAccount("Rahul", 1002, 12000),
    BankAccount("Kiran", 1003, 8000)
]

while True:

    # Display menu options
    print("1.Add Account\n2.Deposit\n3.Withdraw Money\n4.Show Balance\n5.Show All Accounts\n6.Exit")

    choose = int(input("Enter what you want: "))

    # Create a new account
    if choose == 1:
        name = input("Enter your name: ").lower()
        acc_no = int(input("Enter acc no: "))
        amount = int(input("Enter the amount you need to deposit as a opening amount: "))

        BankAccount.add_account(name,acc_no,amount)

    # Deposit money into account
    elif choose == 2:
        name = input("Enter your name: ").lower()
        acc_no = int(input("Enter acc no: "))
        amount = int(input("Enter the amount you need to deposit: "))

        BankAccount.deposit(name,acc_no,amount)

    # Withdraw money from account
    elif choose == 3:
        name = input("Enter your name: ").lower()
        acc_no = int(input("Enter acc no: "))
        amount = int(input("Enter the amount to withdraw: "))

        BankAccount.withdraw(name,acc_no,amount)

    # Check account balance
    elif choose == 4:
        name = input("Enter your name: ").lower()
        acc_no = int(input("Enter acc no: "))

        BankAccount.show_balance(name,acc_no)

    # Display all accounts
    elif choose == 5:
        BankAccount.show_accounts()

    # Exit program
    elif choose == 6:
        print("Exiting...")
        break

    else:
        print("You need to choose between (1-6):")