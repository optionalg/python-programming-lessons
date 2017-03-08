# Edit's program converts temperature to Fahrenheit from Celsius and vica versa

def print_options() :
    print("Options:")
    print(" 'c' Would you like to convert Fahrenheit from Celsius?")
    print(" 'f' Would you like to convert from Fahrenheit to Celsius?")
    print(" 'e' Exit")

def celsius_to_fahrenheit(c_temp):
    return 9.0 / 5.0 * c_temp + 32

def fahrenheit_to_celsious(f_temp):
    return (f_temp - 32.0) * 5.0/9.0


choice = "p"
while choice != "e":
    if choice == "c":
        c_temp = float(input("Please give a Celsius temperature: "))
        print("Here is your entered Celsius in Fahrenheit: ", celsius_to_fahrenheit ( c_temp))
        choice = input("option: ")
    elif choice == "f":
         f_temp = float(input("Please give a Fahrenheit temperature: "))
         print("Here is your entered Fahrenheit in Celsius: ", fahrenheit_to_celsious (f_temp))
         choice = input ("option: ")
    else:
         choice = "p"  #Alternatively choice != "q": so that print
                       #when anything unexpected inputed
         print_options()
         choice = input("option: ")
         
