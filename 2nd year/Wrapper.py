def report_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        print("        DYNAMIC REPORT GENERATOR")
        print("=" * 50)
        func(*args, **kwargs)
        print("=" * 50)
        print("          END OF REPORT")
        print("=" * 50)
    return wrapper


class Report:
    college = "MIT Engineering College"

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name

    def __str__(self):
        return (
            f"Name      : {self.name}\n"
            f"Roll No   : {self.roll}\n"
            f"Marks     : {self.marks}"
        )

    @report_header
    def display_report(self):
        print(f"College   : {Report.college}")
        print(self)

        if self.marks >= 40:
            print("Result    : Pass")
        else:
            print("Result    : Fail")


student1 = Report("Malhar", 69, 41)
student1.display_report()

print()

Report.change_college("MIT ADT College of Engineering")

student2 = Report("Anu", 56, 98)
student2.display_report()