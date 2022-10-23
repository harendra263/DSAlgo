'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''


n = int(input("Enter number of rows:  "))

for row in range(1, n + 1):
    col = 1
    while col<=row:
        print(end="* ")
        col += 1
    print()



