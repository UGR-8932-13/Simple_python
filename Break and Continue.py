############# break #######################
###### For Loop
"""for i in range(0,100):
    if i > 50:
        break
    print(i)"""
###### While Loop
"""while True:
    n = input("Enter num or press q for quit:")
    if n == "q":
        break"""
########## Continue ######################
###### For
"""for i in range(0,4):
    if i == 2:
        continue
    print(i)"""
###### While
n = 0
while n <=10:
    n+=1
    if n%2 != 0:
        continue
    print(n)

    