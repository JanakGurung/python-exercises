from phone import Phone

# TODO how do i implement my inventory?
phone_inventory = [Phone("Pixel 8", "Google", 45000, "16 GB", 23),
                    Phone("Iphone 12", "Apple", 120000, "16 GB", 523),
                    Phone("te", "testbrand2", 22355, "teststorage2", 223)]

# TODO add a phone inventory
# TODO ask the phone details from user before adding the phone to inventory
#TODO need to handle exceeption
# TODO how to prevent duplicate phone model
def add_phone():
    model= input("Enter the phone model:")
    brand= input("Enter the phone brand:")
    price= input("Enter the phone price:")
    storage= input("Enter the phone storage:")
    quantity= input("Enter the phone quantity:")

    phone = Phone(model, brand, price, storage, quantity)


    phone_inventory.append(phone)

# print(phone_inventory)

#these are changes from main branch

# TODO view details of a phone
# TODO how do i show the information of the phone that the user wants.
def view_phone_details():
    i = 1
    print("-----------------------------------") #customizing the view
    print("| Phone Model   |  Brand  | Storage  |  Price  |  Quantity")
    for phone in phone_inventory:
        print(f"| {i} |{phone.get_model()} |  {phone.get_brand()} | {phone.get_storage()} | {phone.get_price()} | {phone.get_quantity()}")
        i = i+1


# TODO update detail of phone
def update_phone_details():
    model_number_to_update = input("Enter the phone model number: ")
    for phone in phone_inventory:
        if model_number_to_update == phone.get_model():
            new_model_number = input("Enter model number: ")
            new_brand = input("Enter brand:")
            phone.set_model(new_model_number)
            phone.set_brand(new_brand)
            print(f"{model_number_to_update} has been updated.")
            return
        
    print(f"{model_number_to_update} not found in records\n")
        
   
   
   
#TODO delete a phone
def delete_phone():
    model_number_to_delete = input("Enter the phone model to delete: ")
    for phone in phone_inventory:
        if model_number_to_delete == phone.get_model:
            phone_inventory.remove(phone)
            print(f"{model_number_to_delete} has been removed from the records....\n")
            return
       
    print(f"{model_number_to_delete} not found in the records ... \n")
    

#TODO how to allow users to do the operations?
#TODO how to let the useer use the program as musch as they want?
#TODO how to let the user to exit the program?
def menu():
    while(True):
        print("Enter 1 to add phone: ")
        print("Enter 2 to view phone details: ")
        print("Enter 3 to update phone detail: ")
        print("Enter 4 to remove a phone: ")
        print("Enter 5 to exit: ")
        try:
            option = int(input("Choose an option: "))
            if(option == 1):
                add_phone()
            elif(option == 2):
                view_phone_details()
            elif(option == 3):
                update_phone_details()
            elif(option == 4):
                delete_phone()
            elif(option == 5):
                print("Thank you, See You Again!!")
                break
            else:
                print("Enter the options from (1 to 5): \n")
        except ValueError:
            print("Invalid Entry!!! Enter from 1 to 5 ..") #exceeption handling
        except:
            print("Cannot perform the action!!")
        
if __name__ == '__main__': #to execute the file only when used when a module is imported to another module, then the python interpretor will assign the string with the name of the module  to the special variabole name.
    menu()
        