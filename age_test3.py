country1 = "the USA"
age1 = 21
country2 = "the Netherlands"
age2 = 18
country3 = "Japan"
age3 = 20

user_country = input(f"Are we in {country1}, {country2} or {country3}? ")

if user_country.lower() not in country1.lower() and \
                user_country.lower() not in country2.lower() and \
                user_country.lower() not in country3.lower():
    print(f"I don't know {user_country}. I'm either stupid or you're already drunk.")
else:
    user_age = int(input("How old are you? "))

    if user_age < age1 and user_country.lower() in country1.lower():
        print(f"Sorry, {user_age} is too young to drink in {country1}!")
    elif user_age < age2 and user_country.lower() in country2.lower():
        print(f"Sorry, {user_age} is too young to drink in {country2}!")
    elif user_age < age3 and user_country.lower() in country3.lower():
        print(f"Sorry, {user_age} is too young to drink in {country3}!")
    else:
        print("Go ahead.")
