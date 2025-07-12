year = int(input("Enter year: "))
# year = 2023

# if (year % 4 == 0 and year % 100 != 0):
#     print(year," is a Leap Year")
if () or (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year," is a Leap year.")
else:
    print(year, "is NOt a Leap year.")