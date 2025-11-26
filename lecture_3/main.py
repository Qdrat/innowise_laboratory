"""
The Student Grade Analyzer

This module provides a console-based application for managing student grades,
including adding students, recording grades, generating reports, and finding top performers.
"""

from typing import List, Dict


def validate_name(name: str) -> bool:
    """Student Name Validation"""
    if not name:
        print("Error: Name cannot be empty!")
        return False
    if any(char.isdigit() for char in name):
        print("Error: Name cannot contain numbers!")
        return False
    if len(name) < 2:
        print("Error: Name is too short!")
        return False
    return True


def add_new_student(students) -> None:
    """Adds a new student to the system"""
    name: str = input("Enter student name: ").strip().title()

    if not validate_name(name):
        return
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Student '{name}' already exists!")
            return
    new_student = {"name": name, "grades": []}
    students.append(new_student)


def add_grades_for_student(students) -> None:
    """Adds a new student to the system"""
    if not students:
        print("Error: There are no students in the system. Add the students first.")
        return

    name = input("Enter student name: ").strip().title()
    if not validate_name(name):
        return

    student_found = None
    for student in students:
        if student["name"].lower() == name.lower():
            student_found = student
            break

    if not student_found:
        print("Error: Student not found.")
        return

    while True:
        grade_input: str = input("Enter a grade (or 'done' to finish): ").lower()
        try:
            if grade_input == "done":
                break
            if 0 <= int(grade_input) <= 100:
                student_found["grades"].append(int(grade_input))
            else:
                print("Error: grade muss 0 - 100")

        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_full_report(students) -> None:
    """Generates a full report on all students"""
    if not students:
        print("Error: There are no students to report.")
        return

    print("-" * 3 + " Student Report " + "-" * 3)
    all_grade_of_student = []
    for student in students:
        try:
            average_grade = float(sum(student["grades"]) / len(student["grades"]))
            print(f"{student['name']} average grade is {average_grade:.1f}.")
            all_grade_of_student.append(average_grade)
        except ZeroDivisionError:
            print(f"{student['name']} average grade is N/A")
    print("-" * 20)
    print(f"Max Average: {max(all_grade_of_student):.1f}")
    print(f"Min Average: {min(all_grade_of_student):.1f}")
    print(
        f"Overall Average: {float(sum(all_grade_of_student) / len(all_grade_of_student)):.1f}"
    )


def find_top_performer(students) -> None:
    """Finds the student with the highest average score"""
    if not students:
        print("Error: There are no students to report.")
        return

    try:
        students_with_grades = [student for student in students if student["grades"]]
        top_student = max(
            students_with_grades,
            key=lambda value: sum(value["grades"]) / len(value["grades"]),
        )
        avg_grade = sum(top_student["grades"]) / len(top_student["grades"])
        print(
            f"The student with the highest average is {top_student['name']} "
            f"with a grade {avg_grade:.1f}"
        )
    except ValueError:
        print("Error: There are no students with grades.")


def show_menu(students) -> None:
    """The main menu of the program"""
    while True:
        print("\n" + "-" * 3 + " Student Grade Analyzer " + "-" * 3)
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find top performer")
        print("5. Exit")

        choice = input("\nEnter your choice: ")
        try:
            if choice == "1":
                add_new_student(students)
            elif choice == "2":
                add_grades_for_student(students)
            elif choice == "3":
                generate_full_report(students)
            elif choice == "4":
                find_top_performer(students)
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Error: Wrong choice! Please select from 1 to 5.")
        except Exception as e:
            print(f"Unexpected error: {e}")


def main() -> None:
    """The main function of the programs"""
    students: List[Dict] = []
    show_menu(students)


if __name__ == "__main__":
    main()
