def check(question, solution_list):
    good_answer = False
    while not good_answer:
        answer = input(question)
        if answer in solution_list:
            good_answer = True
        else:
            print("Please try again!")
           

alarm_codes = ["1234", "4321", "0000"]

check("Have you closed the doors? yes / no\n", ["y", "yes"])
check("Have you turned the lights off? yes / no\n", ["y", "yes"])
check("Enter the alarm code:\n", alarm_codes)

print("Good to go.")  
