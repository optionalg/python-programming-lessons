def check(question, solution_list, tries):
    attempts = 0
    while attempts < tries:
        answer = input(question)
        if answer in solution_list:
            return True
        else:
            print("Please try again!")
            attempts += 1

    print("Wow... Maybe try again later?")
    return False

alarm_codes = ["1234", "4321", "0000"]
doors_closed = False
lights_off = False
alarm_code_correct = False

while not doors_closed or not lights_off or not alarm_code_correct:
    if not doors_closed:
        doors_closed = check("Have you closed the doors? yes / no\n", ["y", "yes"], 3)
    if not lights_off:
        lights_off = check("Have you turned the lights off? yes / no\n", ["y", "yes"], 3)
    if not alarm_code_correct:
        alarm_code_correct = check("Enter the alarm code:\n", alarm_codes, 4)

print("Good to go.")  
