#TODO create a classs name Phone
# with private attributes brand , model, model number, price, storage
# create setter and getter for the private attributes

class Phone:
    def __init__(self, model:str, brand:str, price:int, storage:str, quantity:int):
        self.__brand= brand
        self.__model = model
        self.__price = price
        self.__storage = storage
        self.__quantity = quantity
    
    def set_brand(self, brand:str):
        self.__brand = brand
    
    def get_brand(self):
        return self.__brand
    
    def set_model(self, model):
        self.__model = model
    
    def get_model(self):
        return self.__model
    
    def set_price(self, price):
        self.__price = price
    
    def get_price(self):
        return self.__price
    
    def set_storage(self, storage):
        self.__storage = storage
    
    def get_storage(self):
        return self.__storage
    
    def set_quantity(self, quantity: int):
        self.__quantity = quantity
    
    def get_quantity(self):
        return self.__quantity


# phone = Phone("Apple", "15 pro", "Rs.98,000", "512 GB", "10")

# print(phone.get_price())