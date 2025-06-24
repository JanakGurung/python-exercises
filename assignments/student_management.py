from student import Student
import re

student_management = [Student("Alice", 101, 10, 9812345678,"alice@gmail.com"),
                        Student("Scott", 102, 9, 9870987652, "scott@gmail.com"),
                      Student("Chris", 103, 10, 9876512341, "chris@yahoo.com")]

def validate_email_regex(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True
        else:
            return False

#add studnet
def add_student():
    while (True):
        full_name = input("Enter name: ").strip()
        if full_name:
            break
        else:
            print("Name cannot be empty.")

    while (True):
        try:    
            roll_number = int(input("Enter Roll number: "))
            if roll_number <= 0:
                print("Roll number must be positive.")
            elif roll_number > 9999:
                print("Roll number too large. Please use the value less than 10000.")
            elif duplicate_roll(roll_number):
                print("Student with this roll number already exists.")
            else:
                break
        except ValueError:
            print("Invalid Roll number. Enter an integer.")
        
        
    grade = int(input("Enter grade: "))
    
    while (True):
        try:
            phone_number = int(input("Enter phone number: "))
            break
        except ValueError:
            print("Invalid Phone number")
            
    
    while (True):
        email_address = input("Enter email address: ")
        if validate_email_regex(email_address):
            break
        else:
            print(f"{email_address} is an invalid email format.")  
    
    student = Student(full_name, roll_number, grade, phone_number, email_address)

    student_management.append(student)
    print("Student added successfully.")

#avoiding duplicate roll number function   
def duplicate_roll(roll_number):
    return any(student.get_roll_number() == roll_number for student in student_management)
    
# view student details
def view_students():
    if not student_management:
        print("no records found.")
        return
    i= 1
    print("-------------------------")
    print("|S.no.| Name | Roll |Grade| Phone number | Email address")
    for student in student_management:
        print(f"|  {i}  | {student.get_full_name()} | {student.get_roll_number()} | {student.get_grade()} | {student.get_phone_number()}  |  {student.get_email_address()} ")
        i <= 4
        i += 1


#update student       
def update_student_grade():
    try:
        student_to_update = int(input("Enter the roll no. : "))
    except ValueError:
        for student in student_management:    
            if student_to_update == student.get_roll_number():
                new_roll_number = int(input("Enter new roll number: "))
                if new_roll_number:
                    try:
                        new_roll = int(new_roll_number)
                        if new_roll <= 0:
                            print("roll number must be positive.")
                            return
                        elif duplicate_roll(new_roll):
                            print("Roll number already exists. Update cancelled")
                            return
                        else:
                            student.set_roll_number(new_roll)
                    except ValueError:
                        print("Invalid input. Update cancelled")
            
                        
                            
                        
            new_grade= int(input("Enter new grade: "))
            if new_grade:
                try:
                    new_grade = int(new_grade)
                    student.set_grade(new_grade)
                except ValueError:
                    print("Invalid input for grade. Update Cancelled")
                    return
                    
            
            print(f"Student updated successfully.")
            return
    print("Student not found.")
            
# delete student
def delete_student():
    try:
        student_to_delete = int(input("Enter the Roll: "))
    except ValueError:
        return
    for student in student_management:
        if student_to_delete == student.get_roll_number():
            student_management.remove(student)
            print("Student deleted successfully.  \n")
            return
    print(f"{student_to_delete} no student found with this roll number. \n")

    
    


# menu        
def menu():
    while (True):
        print("Enter 1 to Add a student: ")
        print("Enter 2 to View students: ")
        print("Enter 3 to Update a student: ")
        print("Enter 4 to delete a student: ")
        print("Enter 5 to Exit: ")
       
        option = int(input("Choose an option: "))
        if (option == 1):
            add_student()
        elif (option == 2):
            view_students()
        elif (option == 3):
            update_student_grade()
        elif (option == 4):
            delete_student()
        elif (option == 5):
            print("Application terminates gracefully.")
            break
        else:
            print("Enter the options from (1 to 5)")
 
if __name__ == "__main__":
    menu()               

