# Temperature conversion

def menu():
    print("\nl. Celcius to Fahrenheit")
    print("2. Fahrenheit to Celcius")
    print("3. Exit")
    return int(input("Enter a choice: "))
    

def toCelsius(f):
    return int((f-32) / 1.8)

def toFahrenheit(c):
    return int(c * 1.8 +32)
             
def main():
    choice = menu()
    while choice != 3:
        if choice == 1:
            # convert C to F
            c = eval(input("Enter degrees Celsius: "))
            print(str(c) + "C = " + str(toFahrenheit(c)) + "F")
        elif choice == 2:
            # convert F to C
            f = eval(input("Enter degrees Fahrenheit:"))
            print(str(f) + "F = " +str(toCelsius(f)) + "C")
        else:
            print("invalid entry")
        choice = menu()

main()
