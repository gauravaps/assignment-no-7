# write python script to check whether a given number is positive ,negative or zero using match case statement.

'''w= int(input("enter a number"))
match w:

    case w if w>0:
        print("positive")

    case w if w<0:
        print('negative')
    case w if w ==0:
        print("zero")
    case _:
        print("default") '''

num=int(input("enter a number"))

if num >0:
    print("positive number")

elif num<0:
    print("negative number")

elif num==0:
    print('number zero')

   
