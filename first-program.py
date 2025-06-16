# write a program to check the sum of two numbers provided by useer is even or not using functions.
def add(a,b):
    return a+b
    
def check_even(number):
    if number %2== 0 :
        return True
    else:
        return False
    
#TODO ask two numbers form users
first_number= int(input("Enter first number\n"))
second_number =int(input("Enter second number\n"))  

#TODO find the sum using add function
sum= add(first_number, second_number)   

#TODO check if the sum is even or not
if check_even(sum):
    print("even")
else:
    print("odd")