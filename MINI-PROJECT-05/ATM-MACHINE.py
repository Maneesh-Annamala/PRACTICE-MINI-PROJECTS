# Deposit money
def to_deposit(balance):
    """Deposit money into account."""

    try:
        deposit = int(input("Enter the money: "))

    except ValueError:
        print("Please enter only numbers!")
        return balance

    # Validate amount
    if deposit <= 0:
        print("enter valid amount")
        return balance

    balance += deposit
    deposit_history.append(deposit)

    print(f"You deposited {deposit}Rs and it was successful")

    return balance


# Withdraw money
def to_withdrawl(balance):
    """Withdraw money from account."""

    try:
        withdraw = int(input("Enter the withdrawl amount: "))

    except ValueError:
        print("Please enter only numbers!")
        return balance

    # Validate amount
    if withdraw <= 0:
        print("enter valid amount")
        return balance

    # Check balance
    elif withdraw > balance:
        print("Insufficient balance!")

    else:
        balance -= withdraw
        withdrawl_history.append(withdraw)

        print(f"you withdraw {withdraw}Rs now you have {balance}")

    return balance


# Show transaction history
def history(deposit_his, withdrawl_his):
    """Display deposit and withdraw history."""

    print("please wait we are fetching your details☺")

    return (
        f"Here is you deposit history:\n{deposit_his}"
        f"\nHere is your withdrawl history:\n{withdrawl_his}"
    )


balance = 1000
deposit_history = []
withdrawl_history = []
over = False

while not over:

    try:
        # Show menu
        choose = int(input(
            "1.Deposit\n2.Withdrawl\n3.Balance Check\n4.Transaction history\n5.Exit\nwhat do you want to do please choose between these:"
        ))

    except ValueError:
        print("Please choose between them☺")
        continue

    # Deposit money
    if choose == 1:
        balance = to_deposit(balance)

    # Withdraw money
    elif choose == 2:
        balance = to_withdrawl(balance)

    # Show balance
    elif choose == 3:
        print(f"This is your current balance {balance}Rs")

    # Show transaction history
    elif choose == 4:
        print(history(deposit_history, withdrawl_history))

    # Exit program
    elif choose == 5:
        over = True
        print("Thank you!")

    else:
        print("You chose invalid option")