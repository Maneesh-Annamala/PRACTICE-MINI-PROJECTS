# Show spending percentage
def show_percentage(data, total):
    """Display spending percentage for each category."""

    for k in data:
        percent = (data[k] / total) * 100
        print(f"{k} : {percent:.2f}%")


expenses = {}
total = 0
highest_category = ""
highest = float("-inf")
lowest_category = ""
lowest = float("inf")
is_on = True

# Get budget
while True:
    try:
        budget = int(input("Enter your budget: "))
        break

    except ValueError:
        print("you need to enter only integers")

while is_on:

    # Get category and amount
    category = input("Enter the category that you spent: ").lower()

    try:
        amount = int(input("Enter the amount: "))

    except ValueError:
        print("please enter only numbers")
        continue

    # Validate amount
    if amount <= 0:
        print("please enter amount greater than 0")

    else:
        # Add expense
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

        total += amount

        # Ask to continue or quit
        quit_add = input(
            "Do you want to add or quit? Type 'y' to quit 'n' to add:"
        ).lower()

        while quit_add not in ["y", "n"]:
            quit_add = input(
                "Choose only between 'y' and 'n': "
            ).lower()

        if quit_add == "y":
            is_on = False

        # Stop if budget exceeded
        if total > budget:
            is_on = False
            print("You exceeded your budget")

# Handle empty expenses
if len(expenses) == 0:
    print("No expenses added")

else:
    # Find highest and lowest spending
    for on_what, money in expenses.items():

        if money > highest:
            highest = money
            highest_category = on_what

        if money < lowest:
            lowest = money
            lowest_category = on_what

    # Show results
    print(f"Total expenses: {total}")
    print(f"Highest spent category is {highest_category} with {highest}")
    print(f"Lowest spent category is {lowest_category} with {lowest}")

    print("The percentage categories")
    show_percentage(expenses, total)