# Add student details
def add_students():
    """This function is used to take student data and store it in dictionary format"""
    student_details = {}

    # Get number of students
    num_of_students = int(input("Enter number of students: "))

    # Store student name and marks
    for i in range(num_of_students):
        names = input("Enter the student name: ")
        marks = int(input("Enter the marks: "))
        student_details[names] = marks

    return student_details

# Find topper student
def topper_student(students):
    """This function is used to find the topper student"""
    marks = float("-inf")
    name = ""

    # Compare marks to find topper
    for i in students:
        if students[i] > marks:
            marks = students[i]
            name = i

    return f"The topper of the exam is {name} with {marks} marks"

# Find second highest student
def second(students):
    """To know about the second rank"""
    highest = float("-inf")
    second_highest = float("-inf")
    highest_name = ""
    second_name = ""

    # Find highest and second highest marks
    for i in students:
        if students[i] > highest:
            second_highest = highest
            second_name = highest_name
            highest = students[i]
            highest_name = i

        elif students[i] > second_highest and students[i] != highest:
            second_highest = students[i]
            second_name = i

    # Handle case where second rank is not available
    if second_name == "":
        return "There is no second rank"

    return f"second highest {second_highest} for {second_name}"

# Calculate average marks
def avg_marks(students):
    """This function calculates the average marks of students"""
    average = 0
    total = 0

    # Add all marks
    for i in students:
        total += students[i]

    average = total / len(students)
    return average

# Find failed students
def failed_students(students):
    """To find the list of failed students"""
    failed = []

    # Check marks below passing score
    for i in students:
        if students[i] < 35:
            failed.append(i)

    # Handle case when no one failed
    if len(failed) == 0:
        return "There is no failed students"

    return failed

# Get student data
students_data = add_students()

# Display results
print(students_data)
print(topper_student(students_data))
print(second(students_data))
print(avg_marks(students_data))
print(failed_students(students_data))