import random




# num = input("Enter a number")
# x = int(num) % 2
# if x > 0:
#     print("You picked even number")
# else:
#     print("You picked odd number")
# ctrl + k,c comment 
# ctrl + k,u revert comment

# a = []
# b = []
# c = set()

# for i in range(0,100):
#     n= random.randint(1,100)
#     a.append(n)
    
# for x in a:
#     if x % 2 ==0:
#        b.append(x) 

# for x in b:
#     if x > 50:
#         c.add(x)

# for element in c:
#     print(c)

y = []

for i in range(1):
    for i in range(0,10):
        y.append(i)
        print(y)
    while y:
        y.pop()
        print(y)

for i in range(5):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
