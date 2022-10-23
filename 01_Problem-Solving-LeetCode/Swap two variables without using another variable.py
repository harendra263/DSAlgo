# Swap two variables without using another variable
b = 5

a = 10 + b
b = a - b
a -= b

print(f"a = {a}")
print(f"b = {b}")


'''
a = 5
b = 10
'''