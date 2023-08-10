import random 


x=random.randint(1,100)

while True:

    y=int(input("enter youre number:"))
    if y==x:
        print("you guessed it right")
        exit()
    elif y<x:
        print("try increasing")
    else:
        print("try decreasing")





