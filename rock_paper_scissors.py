# pylint: disable=C0103

# 2 players
# 3 possibles answers: rock, paper, scissors
# rock > scissors > paper > rock ...

# ask the players their name
# ask their choice
# check their choice (needs to be valid)
# find a way to hide the choice???? (print many lines)
# compare the choices
# announce the winner

# loop to play several times
# have a way to exit the program
# scores

# high scores (in a file)
# extend the game: add more choices (lizard, spock...)

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


choice1 = check(player1 + ": enter your choice (rock, paper or scissors)",
                ["rock", "paper", "scissors"])
choice2 = check(player2 + ": enter your choice (rock, paper or scissors)",
                ["rock", "paper", "scissors"])

print(player1 + " choice is " + choice1)
print(player2 + " choice is " + choice2)
