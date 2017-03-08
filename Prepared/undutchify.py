# complicated way
dutch_name = input("Please enter your Dutch name: ")
new_name = ""

vowels = ["e", "u", "o", "a"]

i = 0

while i < len(dutch_name):
    if (dutch_name[i] == "i" 
    and i < len(dutch_name)-1
    and dutch_name[i+1] == "j"):
        new_name += "y"
        i += 2
    elif(dutch_name[i] in vowels
    and i < len(dutch_name)-1
    and dutch_name[i+1] == dutch_name[i]):
        new_name += dutch_name[i]
        i += 2
    else:
        new_name += dutch_name[i]
        i += 1
        
print("Your new name is: " + new_name)
