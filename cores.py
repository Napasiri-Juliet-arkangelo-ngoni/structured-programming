input("Enter scores strictly between 100 and 0")
mark = int(input("please enter the number between 0 abd 100"))

if mark >= 90 and mark <= 100:
    print(" Your grade is D1")
elif mark >= 80 and mark <= 89:
    print("Your grade is D2")
elif mark >= 70 and mark <= 79:
    print("Your grade is C3")
elif mark >= 60 and mark <= 69:
    print("Your grade is C4")        
elif mark >= 50 and mark <= 59:
    print("Your grade is C5")
elif mark >= 45 and mark <= 49:
    print("Your grade is C6")
elif mark >= 40 and mark <= 44:
    print("Your grade is P7")
elif mark >= 35 and mark <= 39:
    print("Your grade P8")
elif mark >= 0 and mark <= 34:
    print("Your grade F9")
else:
    print("Invalid mark . Please enter a value between 0 and 100.")
        
            
        
        
        
                       