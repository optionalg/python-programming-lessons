# pylint: disable=C0103

def check(question, solutions):
    """
    ask a question to the user, and check that their answer is in the solutions
    """
    good_answer = False
    while not good_answer:
        answer = input(question)
        if answer in solutions:
            good_answer = True
        else:
            print("Please try again!")


alarm_codes = ["1234", "4321", "0000"]

check("Have you closed the doors? yes / no ", ['yes', 'y'])
check("Have you turned off the lights? yes / no ", ['yes', 'y'])
check("Enter the alarm code: ", alarm_codes)

print("Good to go!")
