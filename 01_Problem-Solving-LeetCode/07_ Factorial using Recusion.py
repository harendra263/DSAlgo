def fact(n):
    return 1 if n ==0 else n*fact(n-1)
    
n = int(input("Write the number: \n"))
print(f"Factorial of {n} is: {fact(n)}")

