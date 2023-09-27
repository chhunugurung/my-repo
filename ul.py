try:
    score = float(input("Enter your score:"))
except:  
    print("Enter a valid score")
if (score > 0 and score <= 100):  
    if (score >= 90): 
        grade = "A"
    elif (score >= 80):
        grade= "B" 
    elif (score >= 70):
        grade= "C" 
    elif (score >= 60):
        grade= "D" 
    elif (score < 60):
        grade= "F" 
    print("your grade is ",grade)
else:
    print("enter your score between 0 to 100")