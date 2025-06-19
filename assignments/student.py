class Student:
    def __init__(self, full_name, roll_number, grade, phone_number, email_address):
        self.__full_name = full_name
        self.__roll_number = roll_number
        self.__grade = grade
        self.__phone_number = phone_number
        self.__email_address = email_address
        
    def set_full_name(self, full_name):
        self.full_name = full_name
        
    def set_roll_number(self, roll_number):
        self.roll_number = roll_number
    
    def set_grade(self, grade):
        self.grade = grade
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    
    def set_email_address(self, email_address):
        self.email_address = email_address
        
    def get_full_name(self):
        return self.__full_name
    
    def get_roll_number(self):
        return self.__roll_number
    
    def get_grade(self):
        return self.__grade
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_email_address(self):
        return self.__email_address
        