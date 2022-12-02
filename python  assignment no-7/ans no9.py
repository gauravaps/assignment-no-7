#  write a python script to check whether a given year is 
# a.non century leap year.
#b.century leap year .
# c.non century non leap year.
# d. century non leap year.

year=int(input("enter a year"))


match year:
    case year if year %100==0:
        print("century  year ")

    case year if year %100==0 and year%400==0 or year%4==0:
         print(" NON century leap year")


    case year if year%400==0 and year%4==0 and year%100!=0:
        print("century leap year")

    case year if year%400!=0 or year%4!=0 or year%100!=0:
        print("non centure non leap")