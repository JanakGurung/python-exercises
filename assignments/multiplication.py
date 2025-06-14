# Display a multiplication table of the number provided by the user for the desired number.
num= int(input("Enter a Number:"))
print(f"multiplication table for {num} upto 10:") #the variable {num} is replaced by num by the user
for i in range(1,11): #loops from 1 to 10
    print(f"{num} x {i} = {num * i}")