# String is your immutable datatype,i.e; once a string is created inside the memory and allocated a definite space, then it cannot be altertered such that the piece of information remains consistent throughout the program.
# Here we'll be using ptint() function , although while using an IDLE or terminal one can avoid this function.
print('spam')
print("Bobs's messages")
print(b'a\x01c')
print(u'sp\xc4m')

username = "Maneuver" # variable referencing to a string
print(username)

username = "Geekos" # same variable dereferencing to some another string (simply saying: changing the string value reference variable)
print(username)
print("Maneuver") # yet the string "Maneuver" retains an unique reference in the Memory space

# accessing elements of a string

# syntax: stringVar[index of character (e.g; 0 - n)]
print(username[0])
print(username[2])
print(username[-1])
print(username[0-2])

# slicing and chopping

# syntax: strVar[inclusive index : exclusive index]
print(username[1:4])

num_list = "0123456789"
print(num_list[0:4])
print(num_list[3:8])
print(num_list[0:7:2])
print(num_list[0:7:3])

# use of dir() for string refrencing  variables

# refVar = "Fruitful"
# dir(refVar)

# dir("flowerest")

# inside an IDLE, this will return U python string manipulation OR interpolation keywords

# METHODS FOR STRING

strVar = "Test String"
print(strVar)
print(strVar.lower())
print(strVar.upper())

# to Find?
print(strVar.find("String"))

# to find Length
print(len(strVar))

# to find count?
string = " star Star star star star stars Stars"
print(string.count("star"))

stpvar = "  Stripped String  "
print(stpvar.strip())

str_replace = "Place String"
print(str_replace.replace("Place", "Replace"))

strlst = "TATA, Toyota, Honda, Hyudai, Skoda"
print(strlst.split())
print(strlst.split(", "))

# Place Holders {}
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"

print(order)
print(order.format(quantity, chai_type))

chai_variety = ["Lemon", "Masala", "Ginger"]
print(chai_variety) # retuns a list
print("".join(chai_variety)) # returns a string
print("-".join(chai_variety)) # retuns string where each member of the list separated with hyphen
print(", ".join(chai_variety))

# Iterations
h = "Iron Head"
for letter in h:
    print(letter)