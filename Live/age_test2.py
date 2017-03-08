country1 = "Netherlands"
country2 = "USA"

country = input(f"Are we in the {country1} or the {country2}? ") 

if country.lower() != country1.lower() and \
   country.lower() != country2.lower():
    print("I don't know this country")
else:
    age = float(input("How old are you? "))
    if age < 18 and country.lower() == "netherlands":
        print("Too young for the Netherlands")
    elif age < 21 and country.lower() == "usa":
        print("Too young for the USA")
    else:
        print("Please enter the bar")
