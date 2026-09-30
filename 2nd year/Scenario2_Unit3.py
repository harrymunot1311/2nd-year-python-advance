import csv
import os

FILE_NAME = "courses.csv"

def read_courses():
    courses = []

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                courses.append(row)

    except FileNotFoundError:
        print("Error: courses.csv file not found.")

    return courses


def display_courses(courses):
    if not courses:
        print("No course records found.")
        return

    print("\nCourse Records")

    for course in courses:
        print("\nCourse ID   :", course["CourseID"])
        print("Course Name :", course["CourseName"])
        print("Instructor  :", course["Instructor"])
        print("Duration    :", course["Duration"])
        print("Fee         :", course["Fee"])


def search_course(courses):
    course_id = input("Enter Course ID: ")

    found = False

    for course in courses:
        if course["CourseID"].lower() == course_id.lower():
            print("\nCourse Found")
            print("Course ID   :", course["CourseID"])
            print("Course Name :", course["CourseName"])
            print("Instructor  :", course["Instructor"])
            print("Duration    :", course["Duration"])
            print("Fee         :", course["Fee"])

            found = True
            break

    if not found:
        print("Course not found.")


def accept_filename():
    filename = input("Enter a filename: ")

    if os.path.exists(filename):
        print("File exists:", filename)
    else:
        print("File does not exist.")


def main():
    courses = read_courses()

    while True:
        print("\nCourse Information System")
        print("1. Display all course records")
        print("2. Search course by Course ID")
        print("3. Accept filename")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_courses(courses)

        elif choice == "2":
            search_course(courses)

        elif choice == "3":
            accept_filename()

        elif choice == "4":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
