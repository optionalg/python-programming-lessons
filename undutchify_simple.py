name = input("Please enter you Dutch name: ")
vowels = ['a', 'e', 'u', 'i', 'o']

name = name.replace("ij", "y")

for vowel in vowels:
    name = name.replace(vowel * 2, vowel)

print(name)
