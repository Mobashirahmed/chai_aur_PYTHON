# List is your mutable data-type
tea_varieties = ["Black", "Green", "Oolong", "White"]
# copying the list
tea_varieties_copy = tea_varieties.copy()

print(tea_varieties)
print(tea_varieties[0])
print(tea_varieties[1])
print(tea_varieties[-1])
print(tea_varieties[1:3])
print(tea_varieties[:2])
print(tea_varieties[2:])

# updating the list
tea_varieties[1] = "Herbal"
print(tea_varieties)

print(tea_varieties[2:3])
tea_varieties[2:3] = "Lemon"
print(tea_varieties)

# ********  Copied List  ********
     
print(tea_varieties_copy[2:3])
tea_varieties_copy[2:3] = ["Masala"]
print(tea_varieties_copy)

print(tea_varieties_copy[1:1])
tea_varieties_copy[1:1] = ["Herbal", "Pudina"]
print(tea_varieties_copy)

print(tea_varieties_copy[1:2])
print(tea_varieties_copy[1:3])

tea_varieties_copy[1:3] = []
print(tea_varieties_copy)

for tea in tea_varieties_copy:
    print(tea)
    
for tea in tea_varieties_copy:
    print(tea, end="-")
    
# conditional Queationing?
if "Oolong" in tea_varieties_copy:
    print("\nI've Oolong tea")
    
tea_varieties_copy.append("Oolong")

if "Oolong" in tea_varieties_copy:
    print("\nI have Oolong Tea")
    
print(tea_varieties_copy)

# ************METHODS for LIST************

print(tea_varieties_copy.pop()) # returns an echo
print(tea_varieties_copy)
print(tea_varieties_copy.remove("Green")) # returns None
print(tea_varieties_copy)
print(tea_varieties_copy.insert(3, "Green")) # returns None
print(tea_varieties_copy)

#****************ITERATIONS****************
squared_nums = [x**2 for x in range(10)]
print(squared_nums)
cube_nums = [y**3 for y in range(5)]
print(cube_nums)