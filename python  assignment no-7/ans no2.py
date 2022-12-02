#  write a python program to perform following operations - addition, subtraction, multiplication ,division.


operations=int(input("enter your choice"))
    
match operations:
    case 1:
        a=int(input("enter a number "))
        b=int(input("enter  b number "))
        print(a+b)
            
    case 2:
        a=int(input("enter a number "))
        b=int(input("enter  b number "))
        print(a-b)

    case 3:
        a=int(input("enter a number "))
        b=int(input("enter  b number "))
        print(a*b)

    case 4:
        a=int(input("enter a number "))
        b=int(input("enter  b number "))
        print(a//b)

    case 5:
        exit()


    case _:
         print("enter correct operator")