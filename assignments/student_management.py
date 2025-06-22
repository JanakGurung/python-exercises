from student import Student

student_management = [Student("Alice", 101, 10, 9812345678, "alice@gmail.com"),
                      Student("Scott", 102, 9, 9870987652, "scott@gmail.com"),
                      Student("Chris", 103, 10, 9876512341, "chris@yahoo.com")]

#add studnet
def add_student():
    full_name = input("Enter name: ")
    roll_number = input("Enter Roll number: ")
    grade = input("Enter grade: ")
    phone_number = input("Enter phone number: ")
    email_address = input("Enter email address: ")
    
    student = Student(full_name, roll_number, grade, phone_number, email_address)
    
    student_management.append()
    
# view student details
def view_students():
    i= 1
    print("-------------------------")
    print("|S.no.| Name | Roll |Grade| Phone number | Email address")
    for student in student_management:
        print(f"|  {i}  | {student.get_full_name()} | {student.get_roll_number()} | {student.get_grade()} | {student.get_phone_number()}  |  {student.get_email_address()} ")
        i <= 4
        i += 1


#update student       
def update_student_grade():
    student_to_update = input("Enter the roll no. : ")
    for student in student_management:    
        if student_to_update == student.get_roll_no():
            new_roll_number = input("Enter new roll number: ")
            new_grade= input("Enter new grade: ")
            student.set_roll_number()
            student.set_grade()
            print(f"{student_to_update} has been updated.")
            return
        else:
            print(f"{student_to_update} not found in records.")
            
# delete student
def delete_student():
    student_to_delete = input("Enter the Roll: ")
    for student in student_management:
        if student_to_delete == Student.get_roll_number:
            student_management.remove(student)
            print("{student_to_delete} has been deleted from records...\n")
        return
    print(f"{student_to_delete} not found in records...\n")

    
    


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
            print("Student added successfully.")
        elif (option == 2):
            view_students()
        elif (option == 3):
            update_student_grade()
            print("Student updated successfully.")
        elif (option == 4):
            delete_student()
            print("Student deleted successfully.")
        elif (option == 5):
            print("Application terminates gracefully.")
            break
        else:
            print("Enter the options from (1 to 5)")
 
if __name__ == "__main__":
    menu()               
                
        
            
    
        
    
