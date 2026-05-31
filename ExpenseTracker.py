# Track user expenses
def total_expenses(budget):
    """Track expenses and stop if budget exceeds."""

    expenses = 0
    d = {}

    # Welcome message
    print("welcome to the expense tracker")
    print(f"your budget limit is {budget}")

    again = True

    while again:
        try:
            # Get category and price
            name = input("Enter the category: ")
            price = int(input("Enter the price: "))

        except ValueError as e:
            print(e)
            continue

        # Add duplicate category expense
        if name in d:
            d[name] += price
        else:
            d[name] = price

        expenses += price

        # Stop if budget exceeded
        if expenses > budget:
            again = False
            print("you exceeded your limit")
            break

        # Ask for more expenses
        other = input("do you have more? type (y/n): ").lower()

        if other == "n":
            again = False

    print(f"your total expenses: {expenses}")
    return d


# Find highest spending category
def highest_spending(prices):
    """Find the category with highest spending."""

    if len(prices) == 0:
        return "there is no items"

    highest = float("-inf")
    highest_item = ""

    # Compare expenses
    for item in prices:
        if prices[item] > highest:
            highest = prices[item]
            highest_item = item

    return f"{highest_item} is the highest spending category with {highest}"


# Get user budget
budget = int(input("Enter your budget: "))

# Track expenses
spending = total_expenses(budget)

# Show results
print(spending)
print(highest_spending(spending))