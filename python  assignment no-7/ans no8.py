# write a python script to check whether two given string are identical ,first string comes before the second in dictionry order or first string comes after the second string in dictionary order using match case statement.


a=input()
b=input()

match (a,b):
    case (a,b) if a==b:
        print("identical string")

    case (a,b)if(a>b):
        print("{} come after {}".format(a,b))


     
    case (a,b)if(a<b):
        print("{} come after {}".format(b,a))





'''a=input("a ")
b=input('b ')

if a==b:
    print("identical string")

elif(a>b):
    print("{} come after a {}".format(a,b))


     
elif(a<b):
    print("{} come after b {}".format(b,a))'''