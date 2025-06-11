while True:
    try:
        age= int(input("Enter your age:")) 
        if age< 15:
            print(f"{age} is minor")
        elif age>=15:
            print(f'{age} is old')
        else:
            print("enter a proper age")
    except:
        print("please enter numbers")
    run= input("Do you wnat to continue??(y/n)")
    if run =="n":
        break