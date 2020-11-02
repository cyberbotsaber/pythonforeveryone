score = input("Enter Score: ")
if float(score)> 1:
    raise Exception("Sorry, no numbers above 1")
elif float(score) < 0:
    raise Exception("Sorry, no numbers below 0")
elif float(score) >= 0.9:
    grade = 'A'
elif float(score) >= 0.8:
    grade = 'B'
elif float(score) >= 0.7:
    grade = 'C'
elif float(score) >= 0.6:
    grade = 'D'
else:
    grade = 'F'
    
print(grade)
