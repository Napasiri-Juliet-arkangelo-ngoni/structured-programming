#Prompts the user a numeric score.

score = int(input("Enter your score"))

# Determine the grade using the grading scale.
if 80 <= score <= 100:
        grade = "A"
elif 70 <= score < 80:
        grade = "B"
elif 60 <= score < 70:
        grade = "C"
elif 50 <= score < 60:
        grade = "D"
elif 0 <= score < 50: 
        grade = "F"
else:
        grade = "Invalid Score (outside 0-100 range)"

    

