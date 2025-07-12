# TUple OR Tuple

tea_types = ("Black", "Green", "Oolong")
print(tea_types)
print(tea_types[0])
print(tea_types[-1]) # reverse indexing
print(tea_types[1:]) # slicing
print(tea_types[0]) # slicing doesn't affects Indexing

# tea_types[0] = "Lemon"
# print(tea_types)

# ******* RETURNS *******

# Traceback (most recent call last):
#   File "<python-input-2>", line 1, in <module>
#     tea_types[0] = "Tamrind"
#     ~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

print(len(tea_types))
more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)

if "Green" in all_tea:
    print("I have green tea")

more_tea = ("Herbal", "Earl Grey", "Herbal")    
print(more_tea)

print(more_tea.count("Herbal"))

# tuple wrapping
(black, green, Oolong) = tea_types
print(black)
print(green)
print(Oolong)