# pylint: disable=C0103

# 2 players
# 3 possibles answers: rock, paper, scissors
# rock > scissors > paper > rock ...

# ask the players their name
# ask their choice
# check their choice (needs to be valid)
# find a way to hide the choice???? https://stackoverflow.com/questions/2084508/clear-terminal-in-python
# compare the choices
# announce the winner

# loop to play several times
# have a way to exit the program
# scores

# high scores (in a file)
# extend the game: add more choices (lizard, spock...)

import os

# order is important, the next element beasts the current one
choices = ["rock", "paper", "scissors"]

player1 = input('Name of player 1: ')
player2 = input('Name of player 2: ')


def check(question, solutions):
    """
    ask a question to the user, and check that their answer is in the solutions
    """
    while True:
        answer = input(question)
        if answer in solutions:
            return answer
        else:
            print("Please try again!")



def compare(first, second):
    """
    returns 2 if second beats first, 1 if first beats seconds, 0 if they are equal
    """
    if first not in choices or second not in choices:
        print("Error: invalid arguments for compare")
        return None

    index1 = choices.index(first)
    index2 = choices.index(second)

    # check if first equals second, if so return 0
    # check if second beats first
    if index2 == index1 + 1:
        return 2
    # otherwise, first beasts second, return 1


choice1 = check(player1 + ": enter your choice (rock, paper or scissors) ",
                choices)

os.system("cls||clear")

choice2 = check(player2 + ": enter your choice (rock, paper or scissors) ",
                choices)

print(player1 + " choice is " + choice1)
print(player2 + " choice is " + choice2)

print(compare(choice1, choice2))
