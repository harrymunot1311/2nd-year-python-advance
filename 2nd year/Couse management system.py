class Course:
    def __init__(self, name, duration, fee, category):
        self.name = name
        self.duration = duration
        self.fee = fee
        self.category = category
        self.available = True

    def display(self):
        status = "Available" if self.available else "Enrolled"
        print(f"Course: {self.name}, Duration: {self.duration}, Fee: {self.fee}, Category: {self.category}, Status: {status}")


class Student:
    def __init__(self, name):
        self.name = name
        self.enrolled_courses = []

    def display(self):
        print(f"\nStudent: {self.name}")
        if self.enrolled_courses:
            print("Enrolled Courses:")
            for course in self.enrolled_courses:
                print("-", course.name)
        else:
            print("No courses enrolled.")


class Institute:
    def __init__(self):
        self.courses = []
        self.students = []

    def add_course(self, name, duration, fee, category):
        if category != "Short Term" and category != "Long Term":
            print("Invalid category. Choose Short Term or Long Term.")
            return

        course = Course(name, duration, fee, category)
        self.courses.append(course)
        print(f"Course '{name}' added successfully.")

    def register_student(self, name):
        student = Student(name)
        self.students.append(student)
        print(f"Student '{name}' registered successfully.")

    def enroll_course(self, student_name, course_name):
        student = None
        course = None

        for s in self.students:
            if s.name == student_name:
                student = s
                break

        for c in self.courses:
            if c.name == course_name:
                course = c
                break

        if student is not None and course is not None:
            if course.available:
                course.available = False
                student.enrolled_courses.append(course)
                print(f"{student_name} enrolled in '{course_name}'.")
            else:
                print("Course is already enrolled.")
        else:
            print("Student or Course not found.")

    def remove_course(self, student_name, course_name):
        student = None

        for s in self.students:
            if s.name == student_name:
                student = s
                break

        if student is not None:
            for course in student.enrolled_courses:
                if course.name == course_name:
                    course.available = True
                    student.enrolled_courses.remove(course)
                    print(f"{student_name} removed from '{course_name}'.")
                    return
            print("Course was not enrolled by this student.")
        else:
            print("Student not found.")

    def display_courses(self):
        print("\nInstitute Courses:")
        for course in self.courses:
            course.display()


institute = Institute()

institute.add_course("Python Programming", "3 Months", 15000, "Short Term")
institute.add_course("Data Science", "6 Months", 30000, "Long Term")
institute.add_course("Web Development", "4 Months", 20000, "Short Term")

institute.register_student("Rahul")
institute.register_student("Priya")

institute.enroll_course("Rahul", "Python Programming")

institute.display_courses()

institute.remove_course("Rahul", "Python Programming")

institute.display_courses()