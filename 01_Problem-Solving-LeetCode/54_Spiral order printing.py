N = int(input(""))
num = 1
for i in range(N):
    if i%2 ==0:
        for _ in range(5):
            print(num,end=" ")
            num = num + 1
    else:
        num = num+4
        for _ in range(5):
            print(num,end=" ")
            num = num  -1
        num = num+6

    print()

    
    
