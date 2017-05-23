countries = ["France", "Canada", "Netherlands"]

# i = 0
#
# while i < len(countries):
#     print(countries[i])
#     i = i + 1

# ---------------------

# for country in countries:
#     # country = countries[1]
#     print(country)

# ---------------

# name = "Lena"
#
# for letter in name:
#     print(letter, end="")

# ---------------

# names = ["Ann", "Lena", "Bruno", "Luc", "Michelle"]
#
# for name in names[:]:
#     if len(name) < 5:
#         names.remove(name)
#
# print(names)

# --------------

names = ["Ann", "Lena", "Bruno", "Luc", "Michelle"]

i = len(names) - 1

while i >= 0:
    if len(names[i]) < 5:
        del names[i]
    i = i - 1

print(names)





