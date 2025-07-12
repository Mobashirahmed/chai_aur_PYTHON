# {"key1": "value1", "key2": "value2", "key3": "value3"}

chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(chai_types)

#******** Accessing members ********
print(chai_types["Masala"])
print(chai_types.get("Ginger"))
print(chai_types.get("Gingery")) # returns None

chai_types["Green"]= "Fresh" # updating value of a targeted key
print(chai_types)

# ******** Iteration ********
for chai in chai_types:
    print(chai)

for chai in chai_types:
    print(chai_types[chai])
    
for chai in chai_types:
    print(chai, chai_types[chai])
    
for key, value in chai_types.items():
    print(key, value)

# ****** CNDITIONALS ******    
if "Masala" in chai_types:
    print("I have Masala chai")
    
print(len(chai_types)) #returns an integral value denoting the count of no. of items present in the dictionary.

# APPEND, POP, 

chai_types["Earl Grey"] = "Citrus"
print(chai_types)

print(chai_types.pop("Green"))
print(chai_types)

print(chai_types.popitem())
print(chai_types)
print(len(chai_types))

del chai_types["Masala"]
print(chai_types)

tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea": {"Green": "Mild", "Balck": "Strong"}
}

print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])

print(tea_shop.get("Tea"))
print(tea_shop["Tea"].get("Green"))
print(tea_shop.get("Tea").get("Black"))     #returns NONE


index = {54:2465, 76:1239, 93:7342, 87:4354}
print(index)

alphaIndex = {"a":583, "b":941, "f":727, "r":936, "u":307}
print(alphaIndex)

squaredNum = {x: x**2 for x in range(9)}
print(squaredNum)
squaredNum.clear()
print(squaredNum)

keys = ["Masala", "Ginger", "Lemon"]
print(keys)
default_Values = "Delicious"
new_dict = dict.fromkeys(keys, default_Values)
print(new_dict)

values = ["Spicy", "Zesty", "Lime"]
dict2 = dict.fromkeys(keys, values)
print(dict2)