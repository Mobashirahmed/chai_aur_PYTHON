score = int(input("Entre your score: "))

if score >= 101:
    print("Please verify your grade again")
    exit()
# if else LADDERING
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"