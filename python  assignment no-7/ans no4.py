# write a python program which takes user age ans display the category of person.age below 10 years kd,below 20 teen,below 40 young, below 60 exeperienced,age above or equal 60 -senior citizen.

x=int(input("enter a number"))
match x:
     case x if x<=10:
        print("kids")
     case x if x in range(10,20+1):
         print("teen")

     case x if x in range(20,40+1):
         print("young")

     case x if x in range(40,60+1):
         print("old man")

     case x if x>60:
          print("budhhe")

     case _:
           print("enter v=alid")