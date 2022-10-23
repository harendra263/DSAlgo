def computeGCD(a,b):
    return a if b ==0 else computeGCD(b, a%b)

a = int(input("a =  "))
b = int(input("b =  "))

print(computeGCD(a,b))

