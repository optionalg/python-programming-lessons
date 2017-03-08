first_name = "Bruno"
last_name = "Bertomeu"
years = 2
years_text = "years"

if years == 1:
    years_text = "year"


# fix singular / plural for years
print("I'm " + first_name + " " + last_name + " and I've been worked at GameHouse for " +
      str(years) + " " + years_text)

