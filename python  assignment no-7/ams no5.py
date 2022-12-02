# write a python script which taken a number from user.print saurabh shukla it the number is even print prateek jain if the number is negative odd number and print aditya choudhary if the number is positive odd number.
x= int(input("enter a number"))

match x:

    case x if x%2==0:
        print("saurabh shukla")

    case x if x%2!=0 and x<0:
        print("prateek jain")

    case x if x%2!=0 and x>0:
        print("aditya choudhary")        
