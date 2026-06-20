# Problem 3 — Employee Management (OOP)

class Employee:
    """Represents an employee and their salary details."""

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def annual_salary(self):
        """Calculate annual salary."""

        return self.salary * 12

    def display_details(self):
        """Display employee information."""

        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")
        print(f"Annual Salary: {self.annual_salary()}")


# Store employee records
employees = [
    Employee("Maneesh", 50000, "AI"),
    Employee("Vamsee", 40000, "AIML"),
    Employee("Santhosh", 35000, "CSE")
]


while True:

    # Ask user whether to search for an employee
    user_input = input("Do you wanna check employee? Type (y/n): ").lower()

    if user_input == "y":

        user_name = input("Enter the name: ").title()

        found = False

        # Search employee by name
        for employ in employees:

            if employ.name == user_name:
                found = True

                employ.display_details()

        if not found:
            print("We don't have anyone with that name")

    elif user_input == "n":

        print("You choose to exit!")
        print("Exiting...")

        break

    else:
        print("Choose only 'y' or 'n'")