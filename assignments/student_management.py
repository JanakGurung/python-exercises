from student import Student

student_management = [Student("Alice", 101, 10, 9812345678, "alice@gmail.com")]


def add_student():
    full_name = input("Enter name: ")
    roll_number = input("Enter Roll number: ")
    grade = input("Enter grade: ")
    phone_number = input("Enter phone number: ")
    email_address = input("Enter email address: ")
    
    student = Student(full_name, roll_number, grade, phone_number, email_address)
    
    # view student details
def view_students():
    for student in Student:
        print(f"")
    
