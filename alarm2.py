doors_closed = False
lights_off = False
alarm_code_correct = False

alarm_codes = ["1234", "4321", "0000"]

while not doors_closed:
    doors_answer = input("Have you closed the doors? yes / no ")
    if doors_answer == "yes":
        doors_closed = True
    else:
        print("Please close the doors!")

while not lights_off:
    lights_answer = input("Have you turned off the lights? yes / no ")
    if lights_answer == "yes":
        lights_off = True
    else:
        print("Please turn off the lights!")

while not alarm_code_correct:
    code_answer = input("Enter the alarm code: ")
    if code_answer in alarm_codes:
        alarm_code_correct = True
    else:
        print("Wrong alarm code!")

print("Good to go!")
