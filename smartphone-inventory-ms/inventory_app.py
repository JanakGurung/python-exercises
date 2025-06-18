from phone import Phone

# TODO how do i implement my inventory?
phone_inventory = [Phone("model", "brand", 22, "storage", 2)]


# TODO add a phone inventory
# TODO ask the phone details from user before adding the phone to inventory
#TODO need to handle exceeption
def add_phone():
    model= input("Enter the phone model:")
    brand= input("Enter the phone brand:")
    price= input("Enter the phone price:")
    storage= input("Enter the phone storage:")
    quantity= input("Enter the phone quantity:")

    phone = Phone(model, brand, price, storage, quantity)


    phone_inventory.append(phone)

# print(phone_inventory)



# TODO view details of a phone
# TODO how do i show the information of the phone that the user wants.
def view_phone_details():
    for phone in phone_inventory:
        print(f"Phone Model: {phone.get_model()}")
        print(f"Phone Brand: {phone.get_brand()}")
    
# TODO update detail of phone
# TODO delete a phone

#TODO how to allow users to do the operations?
#TODO how to let the useer use the program as musch as they want?
#TODO how to let the user to exit the program?
while(True):
    print("Enter 1 to add phone: ")
    print("Enter 2 to view phone details: ")
    print("Enter 3 to update phone detail: ")
    print("Enter 4 to remove a phone: ")
    print("Enter 5 to exit: ")
    option = int(input("Choose an option: "))
    if(option == 1):
        add_phone()
    elif(option == 2):
        view_phone_details()
    elif(option == 5):
        break
    else:
        print("Enter the options from (1 to 5): \n")
        