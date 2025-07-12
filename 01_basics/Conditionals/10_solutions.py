species = input("Whether is your pet is a Dog OR a Cat: ")
age = int(input("Enter the age of your Pet: "))

if (species == "Dog" and age < 2):
   print("AI recommends you 'Puppy Dog Food' for your pet")
if (species == "Cat" and age > 5):
    print("AI recommends you 'Senior Cat Food' for your pet")