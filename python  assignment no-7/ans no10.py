#Write a program to display day name on the basis of user’s liking of a colour. Ask
#user for his favorite colour. User can answer in a sentence like “I like red colour”.
#Assuming all colour name entered by user is in lowercase. Use match case to display
#day name associated with the colour.
#a. Yellow - Monday
#b. Blue - Tuesday
#c. Orange - Wednesday
#d. White - Thursday
#e. Black - Friday
#f. Red - Saturday
#g. All other colours - Sunday

color=input("enter your favorite colour ")

if color=="yellow":
    print("monday")

elif color=="blue":
    print("tuesday")
elif color=="orange":
    print('wednesday') 

elif color=="white":
    print("thursday")

elif color=="black":

    print("friday")
elif color=="red":
    print("saturday")

else:
    print("all colour is sunday")
    