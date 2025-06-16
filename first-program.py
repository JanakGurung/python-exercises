class Teacher: #creating  a class
    def __init__(self, name ,age): #initializing the attributes of the class
        self.name = name
        self.age = age
    
    def give_assignment(self): #creating the behavior of a class
        print("complete the assignment")
#creating object of the class              
teacher1= Teacher("Sunil", 25)

#accessing the attributes of class
print(teacher1.name)
print(teacher1.age)

#class the function of the class
teacher1.give_assignment()