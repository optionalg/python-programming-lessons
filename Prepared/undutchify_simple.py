name = input("Please enter your Dutch name: ")

vowels = ["e", "u", "o", "a"]

name = name.replace("ij", "y")

for vowel in vowels:
    name = name.replace(vowel*2, vowel)

print("Your new name is: " + name)
    
