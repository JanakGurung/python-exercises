def prime(n):
    if n < 2:
        return False  
    for i in range(2, n):  # 2 to n-1
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
print("is Prime" if prime(num) else "Not Prime")