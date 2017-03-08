name = input("Please enter your name: ")
dutch_name = ""

vowels = ["e", "u", "o", "a"]

for character in name:
    if character == "y":
        dutch_name += "ij"
    elif character in vowels:
        dutch_name += character * 2
    else:
        dutch_name += character
    
print("Your Dutch name is: " + dutch_name)    
