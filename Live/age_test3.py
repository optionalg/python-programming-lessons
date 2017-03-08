country1 = "The Netherlands (NL)"
country2 = "The USA"

country = input(f"Are we in the {country1} or the {country2}? ") 

if country.lower() not in country1.lower() and \
   country.lower() not in country2.lower():
    print("I don't know this country")
else:
    age = float(input("How old are you? "))
    if age < 18 and country.lower() in country1.lower():
        print(f"Too young for {country1}")
    elif age < 21 and country.lower() in country2.lower():
        print(f"Too young for {country2}")
    else:
        print("Please enter the bar")
