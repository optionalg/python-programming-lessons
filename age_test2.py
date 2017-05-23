country = input("Are we in the Netherlands or the USA? ")
age = int(input("How old are you? "))

if age < 18 and country == "Netherlands":
    print("Sorry, " + str(age) + " is too young to drink in the Netherlands!")
elif age < 21 and country == "USA":
    print("Sorry, " + str(age) + " too young to drink in the USA!")
else:
    print("Go ahead.")
