first_name = "Bruno"
last_name = "Bertomeu"
years = 1
years_text = "years"

if years < 2:
    years_text = "year"

# 2 ways of writting it
print("I am " + first_name + " " + last_name + " and I've been working at GameHouse for " + str(years) + " " + years_text + ".")
print("I am {1} {0} and I've been working at GameHouse for {2} {3}.".format(first_name, last_name, years, years_text))
