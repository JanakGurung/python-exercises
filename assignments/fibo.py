# Print the fibonacci sequence for the number of patterns desired by the user.
num= int(input("Enter a number:"))
a,b= 0,1 #first two fibonacci numbers
print("fibonacci sequence:")
for _ in range(num): #loop runs num times
    print(a, end=" ") #all number appear on the same line
    a,b= b, a+b