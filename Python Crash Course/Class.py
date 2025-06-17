class Cafe:
    def __init__(self, cafe_name, cuisine_type): 
        self.cafe_name = cafe_name
        self.cuisine_type = cuisine_type
    
    def describe_cafe(self):
        print(f"{self.cafe_name} is the name of cafe.")
        print(f"{self.cuisine_type} is the type of cuisine served.")
        
    def open_cafe(self):
        print(f"{self.cafe_name} is now open at your service!")
        
#instance of the class
cafe1 = Cafe ("Gurung_cafe", "Nepalese")

#attributes
print(cafe1.cafe_name)
print(cafe1.cuisine_type)

#callin the methods
cafe1.describe_cafe()
cafe1.open_cafe()
        
    
        
                
