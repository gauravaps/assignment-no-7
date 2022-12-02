# write a python script to driven program with the following option.
# a.check whether a given set of three numbers are length of an isosceles triangle or not
# b.check whether a given set of three numbers are length of sides of a right angled triangle or not.
# c. check whether  a given of thre numbers are equilateral triangle or not
# d.exit.

x=int(input("enter any month number"))
match x:
    case x if x in (1,3,5,7,8,10,12):
        print("31 days")

    case x if x in (4,6,9,11):
        print("30 days")

    case 2:
        print("28 days")

    case _:
        print("not valid")