password = input("Enter your password: ")
# password = "Secure3P@ss"
length_password = len(password)

if length_password < 6:
    strength = "Weak"
elif length_password <= 10:
    strength = "Medium"
else:
    strength = "Strong"
    
print("Password strength is : ", strength)