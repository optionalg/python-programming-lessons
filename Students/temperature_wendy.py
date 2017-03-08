# Wendy's temperature converter

def C():
    # c x 9/5 + 32 = F

    c= float(input("please enter the temperature in degrees you would like to convert:"))
    f= c * 9/5 +32
    print("the temperature in degrees celcius was {0}, this is {1} in degrees fahrenheit".format(c,f))

    # (F - 32) x 5/9 = c

def F():
    f= float(input("please enter the temperaturen in degrees F you would like to convert:"))
    fl= f-32
    c= fl *5/9
    print("the temperature in degrees F was {0}, this is {1} in degrees C".format(f,c))
