class Teacher: #creating a class
    def __init__(self, name, age): #initializing the attributes of the class
        self.__name = name #making the attributes private
        self.__age =age
    # usine setter methods to set the values in private attributes   
    def set_name(self, name):
        self.__name = name
    
    # using getter methods to get the values og private attributes
    def get_name(self):
        return self.__name 
    
    def give_assignment(self): #creating the behavior of a class
        print("complete the assignment")
 
 #creating object of the class       
teacher1 = Teacher("Sunil", 25) 

# print(teacher1.age)
# print(teacher1.name)      

#calling the functions of the class
teacher1.give_assignment()
teacher1.set_name("Janak")
print(teacher1.get_name())