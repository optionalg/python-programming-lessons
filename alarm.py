doors_closed = True
lights_off = True

alarm_codes = ["1234", "4321", "0000"]
user_code = "123"

if not doors_closed:
    print("Please close the doors!")
elif not lights_off:
    print("Please turn the lights off")
elif user_code not in alarm_codes:
    print(user_code + " is not the correct alarm code!")
else:
    print("Good to go.")
