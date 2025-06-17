#TODO create a classs name Phone
# with private attributes brand , model, model number, price, storage
# create setter and getter for the price attributes

class Phone:
    def __init__(self, brand, model, price, storage, quantity):
        self.__brand= brand
        self.__model = model
        self.__price = price
        self.__storage = storage
        self.__quantity = quantity
    
    def set_brand(self):
        self.__brand
    
    def get_brand(self):
        return self.__brand
    
    def set_model(self):
        self.__model
    
    def get_price(self):
        return self.__model
    
    def set_price(self):
        self.__price
    
    def get_price(self):
        return self.__price
    
    def set_storage(self):
        self.__storage
    
    def get_storage(self):
        return self.__storage
    
    def set_quantity(self):
        self.__quantity
    
    def get_quantity(self):
        return self.__quantity

