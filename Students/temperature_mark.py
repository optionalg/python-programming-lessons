# This program calculates Fahrenheit based on a given Celcius or vice versa
# credits go to Mark van Kessel + Bruno Bertomeu for knowledge sharing

i = input("Do you want to calculate Celcius (c) or Fahrenheit (f)?")

if i == "f":
    c = input("Give me Celcius and i'll make Fahrenheit: ")
    c2f = int(c) * 1.8 + 32
    print ("Soooo.. that's " + str(c2f) + " Fahrenheit!")

if i == "c":
    f = input("Give me Fahrenheit and i'll make Celcius: ")
    f2c = (int(f) - 32) * 5 / 9
    print ("Soooo.. this looks colder, but you actually won't feel a thing: " + str(f2c) + " Celcius!")
