age = input("Provide me an age: ")

age_in_int = int

if 0 < age_in_int < 13:
    print("Child")    
elif 13 <= age_in_int < 20:
    print("Teenager")
elif 20 <= age_in_int < 60:
    print("Adult")
else:
    print("Senior")