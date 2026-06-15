# Calculate average
def average_of_numbers(total, numbers_list):
    """Return average of all numbers."""

    if len(numbers_list) == 0:
        return "You need to enter data to find average"

    average = total / len(numbers_list)
    return average


# Count even and odd numbers
def even_odd(numbers_list):
    """Count even and odd numbers."""

    even_count = 0
    odd_count = 0

    for i in numbers_list:

        if i % 2 == 0:
            even_count += 1

        else:
            odd_count += 1

    return (
        f"There are {even_count} even numbers\n"
        f"There are {odd_count} odd numbers"
    )


# Find duplicate numbers
def duplicate(numbers_list):
    """Return duplicate numbers."""

    duplicate_numbers = []
    original = []

    for i in numbers_list:

        if i not in original:
            original.append(i)

        elif i in original:

            if i in duplicate_numbers:
                continue

            duplicate_numbers.append(i)

    return f"Duplicate numbers: {duplicate_numbers}"


# Find prime numbers
def prime(numbers_list):
    """Return all prime numbers."""

    prime_numbers = []

    for i in numbers_list:

        if i <= 1:
            continue

        is_prime = True

        for j in range(2, i):

            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(i)

    return f"Prime numbers: {prime_numbers}"


# Get user input
numbers = input("Enter the numbers: ").replace(",", " ").split()
try:
    numbers_list = [int(i) for i in numbers]
except ValueError:
    print("please enter valid input")

highest = float("-inf")
second_highest = float("-inf")
lowest = float("inf")
total = 0

if not numbers_list:
    print("There are no numbers")

else:

    # Find total, highest, second highest and lowest
    for i in numbers_list:

        total += i

        if i < lowest:
            lowest = i

        if i > highest:
            second_highest = highest
            highest = i

        elif i > second_highest and i != highest:
            second_highest = i

    print(f"Highest number is: {highest}")

    if second_highest == float("-inf"):
        print("There is no second highest")

    else:
        print(f"Second highest is: {second_highest}")

    print(f"Lowest number is: {lowest}")
    print(f"Total: {total}")

    print(
        f"Average of numbers: "
        f"{average_of_numbers(total, numbers_list)}"
    )

    print(even_odd(numbers_list))
    print(duplicate(numbers_list))
    print(prime(numbers_list))