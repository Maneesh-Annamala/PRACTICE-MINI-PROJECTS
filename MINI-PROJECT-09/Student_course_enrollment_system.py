class Course:
    """Represents a course offered by the institute."""

    def __init__(self, name, fee):
        self.name = name
        self.fee = fee


class Student:
    """Represents a student and their enrolled courses."""

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

        # Stores enrolled Course objects
        self.courses_data = []

    def enroll(self, course):
        """Enroll a student into a course."""

        self.courses_data.append(course)

        print(f"{self.name} enrolled in {course.name}")

    def show_enrollments(self):
        """Display all courses enrolled by the student."""

        print(f"{self.name}")

        if self.courses_data:

            for course in self.courses_data:
                print(f"-- {course.name}")

        else:
            print("No enrolled courses!")


# Default course records
courses_data = [

    Course("Python", 5000),

    Course("Java", 6000),

    Course("DSA", 7000)

]


# Default student records
students_data = [

    Student("Maneesh", 101),

    Student("Rahul", 102),

    Student("Kiran", 103)

]


while True:

    # Display menu options
    print(
        "1.Add students\n"
        "2.Add courses\n"
        "3.Enroll course\n"
        "4.Display enrolled courses\n"
        "5.Exit"
    )

    choose = int(
        input("Enter what you want by numbers from (1-5): ")
    )

    # Add a new student
    if choose == 1:

        student_name = input(
            "Enter the name of the student: "
        )

        student_rollno = int(
            input("Enter student rollno: ")
        )

        data = Student(
            student_name,
            student_rollno
        )

        students_data.append(data)

    # Add a new course
    elif choose == 2:

        course_name = input(
            "Enter the name of the course: "
        )

        course_fee = int(
            input("Enter the course fee: ")
        )

        data = Course(
            course_name,
            course_fee
        )

        courses_data.append(data)

    # Enroll a student into a course
    elif choose == 3:

        name = input(
            "Enter your name: "
        ).lower()

        roll_no = int(
            input("Enter your rollno: ")
        )

        student_found = None

        # Find student
        for student in students_data:

            if (
                student.name.lower() == name
                and student.rollno == roll_no
            ):
                student_found = student
                break

        if student_found is not None:

            course_found = None

            # Display available courses
            for course in courses_data:
                print(
                    f"{course.name}-{course.fee}"
                )

            name_of_course = input(
                "Enter the course name: "
            ).lower()

            # Find selected course
            for course in courses_data:

                if (
                    course.name.lower()
                    == name_of_course
                ):
                    course_found = course
                    break

            if course_found is not None:
                student_found.enroll(course_found)

            else:
                print("Invalid Entry")

        else:
            print("Invalid Entry")

    # Display all student enrollments
    elif choose == 4:

        for student in students_data:
            student.show_enrollments()

    # Exit program
    elif choose == 5:

        print("Exiting...")
        break

    else:
        print(
            "You need to enter between (1-5) only"
        )