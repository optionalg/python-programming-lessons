dutch_name = input("Please enter you Dutch name: ")
new_name = ""

vowels = ['a', 'e', 'u', 'i', 'o']
i = 0

while i < len(dutch_name):
    # if current letter is vowel and next letter is the same
    # |-> copy that letter
    # |-> increase i by 2
    if dutch_name[i] in vowels and i < len(dutch_name) - 1 and dutch_name[i+1] == dutch_name[i]:
        new_name += dutch_name[i]
        i += 2
    # elif current letter is i and next letter is j
    # |-> copy y
    # |-> increase i by 2
    elif dutch_name[i] == "i" and i < len(dutch_name) - 1 and dutch_name[i+1] == "j":
        new_name += "y"
        i += 2
    else:
        new_name += dutch_name[i]
        i += 1

print(new_name)