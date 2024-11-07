def __init__(self, name, age, grade_level):
        self.name = name
        self.age = age
        self.grade_level = grade_level

def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade Level: {self.grade_level}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade_level = input("Enter student grade level (e.g., 1st year, 2nd year): ")
        student = Student(name, age, grade_level)
        self.students.append(student)
        print("Student added successfully.")

    def remove_student(self):
        name = input("Enter student name to remove: ")
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                print("Student removed successfully.")
                return
        print("Student not found.")

    def search_student(self):
        name = input("Enter student name to search: ")
        for student in self.students:
            if student.name.lower() == name.lower():
                print(f"Student found: {student}")
                return
        print("Student not found.")

    def display_all_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            print("All students:\n")
            for student in self.students:
                print(student)

    def run(self):
        while True:
            print("\nStudent CCIT Information Management System")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Search Student")
            print("4. Display All Students")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.remove_student()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.display_all_students()
            elif choice == '5':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if name == "main":
    sms = StudentManagementSystem()
    sms.run()