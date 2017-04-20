# Bruno's

'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will
turn 100 years old.

Extras:
Add on to the previous program by asking the user for another number and
printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
'''
name = input ("What is your name? ")

print ("Your name is " + name)

age = input ("And what is your age? ")

print ("You are now " + age + " and you will turn 100 years of age in " + str(100 - int(age)) + " years.")

number = input ("Please enter another number: ")

print (int(number) * ("You are now " + age + " and you will turn 100 years of age in " + str(100 - int(age)) + " years."))
