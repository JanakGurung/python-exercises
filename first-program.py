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
        


class Math_Teacher(Teacher):
    def __init__(self, name, age, strict):
        super().__init__(name, age)
        self.__strict = strict
        
    def set_strict(self, strict):
        self.__strict = strict
        
    def get_strict(self):
        return self.__strict
    
    def give_assignment(self):
        print("complete the formula")
    
    
class English_teacher(Teacher):
    def __init__(self, name, age, polite):
        super().__init__(name, age)
        self.__polite = polite
        
    def set_polite(self, polite):
        self.__polite= polite
    
    def get_polite(self):
        return self.__polite
    
    
    
#creating object of the class       
Math_Teacher1 = Math_Teacher("Sunil", 25, "Very Strict")
English_Teacher1= English_teacher("Vishnu", 29, "Very Polite")

# print(teacher1.age)
# print(teacher1.name)      

#calling the functions of the class
Math_Teacher1.give_assignment()
English_Teacher1.give_assignment()
print(English_Teacher1.get_name())
print(Math_Teacher1.get_name())
print(Math_Teacher1.get_strict())
print(Math_Teacher1.give_assignment())
