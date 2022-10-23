'''
       * 
      * * 
     * * * 
    * * * * 
   * * * * * 
  * * * * * * 
 * * * * * * * 
'''

n = int(input("enter no. of rows: "))
for i in range(1, n + 1):
    j = n-i
    while j>=0:
        print(end=" ")
        j = j-1
    print("* "*i)

