## if statements

'''
Syntax

if condition:
    logic
    elif condition
        logic
    else
        logic
    
'''
print("Welcome to number Teller")
number =int(input("please enter a number between 1 to 9"))
if number == 1:
    print("you have entered Number one")
elif number ==1:
    print("you have entered Number two")
elif number ==2:
    print("you have entered Number three")
elif number ==3:
    print("you have entered Number four")
elif number ==4:
    print("you have entered Number five")
elif number ==5:
    print("you have entered Number six")
elif number ==6:
    print("you have entered Number seven")
elif number ==7:
    print("you have entered Number eight")
elif number ==8:
    print("you have entered Number nine")
elif number ==9:
    print("invalid,please enter a number between 1 and 9")




""""

with the use of if statements,write a pythoni program that allows an
instructor to enter strictly between 0 and 9

on receiving the mark, the program has to using a grade based on your
define clusters  80 - 90 is A, 91 -100 is A+ etc.
"""

     print("welcome to mark allocator")
number =int(input("please enter a number between 0 and 100"))
if number < 0 or number > 100:
    print("invalid,no mark")
elif number <= 39:
    print("allocated F")
elif number <= 49:
    print("allocated E")
elif number <= 59:
    print("allocated D")
elif number <= 69:
    print("allocated C")
elif number <= 79:
    print("allocated B")
elif number <= 89:
    print("allocated A")
elif number <= 100:
    print("allocate A+")











