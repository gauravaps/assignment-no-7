# write a python script to check whether a given string is a miltiword string or single word string using match case statement.

'''s=input("enter a string")

match s:
    case s if ' ' in s:
        print("its multiword")
    case s if ' ' not in s:
        print("not multiword")'''
        






s=input("enter a string")

if ' ' in s:
    print("its multiword")
elif ' ' not in s:
    print("not multiword")

else:
    print('empty')   