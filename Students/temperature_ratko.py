#CELSIUS TO FAHRENHEIT CALCULATOR AND VICE VERSA
d = input("Please type what kind of temperature do you want to conver from, Celsius or Fahrenheit? Type c or f: ")
if d == "c" :
    t = float(input("type the temperatures in Celsius: "))
    f = t * 9 / 5 + 32
    print ("temperature in Fahreheit is: ", f)
else:
    t = float(input("type the temperatures in Fahrenheit: "))
    c = (t-32) * 5 / 9
    print ("temperature in Celsius is: ", c)
