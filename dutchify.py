name = input("Please enter your name: ")
dutch_name = ""

vowels = ['a', 'e', 'i', 'o', 'u']

for letter in name:
    if letter == "y":
        dutch_name += "ij"
    elif letter in vowels:
        dutch_name += letter * 2
    else:
        dutch_name += letter

print(dutch_name)
