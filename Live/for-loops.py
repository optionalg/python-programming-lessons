countries = ["France", "Canada", "Netherlands"]

# i = 0
#
# while i < len(countries):
#     print(countries[i])
#     i = i + 1

# ---------------------

# for country in countries:
#     print(country)

# ---------------
# name = "Lena"
#
# for letter in name:
#     print(letter, end="")

# ---------------

names = ["Ann", "Lena", "Bruno", "Luc", "Michelle"]
# names = ["Lena", "Bruno", "Luc", "Michelle"]

for name in names:
    if len(name) < 5:
        names.remove(name)

print(names)
