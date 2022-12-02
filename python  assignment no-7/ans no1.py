


month=int(input("enter any month n4umber"))
match month:
    case month if  month in (1,3,5,7,8,10,12):
        print("31 days")

    case month if month in (4,6,9,11):
        print("30 days")

    case 2:
        print("28 days")

    case _:
        print("not valid")