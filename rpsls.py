import random


def name_to_number(name):
    name = name.lower()

    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4


def number_to_name(num):
    if num == 0:
        return "rock"
    elif num == 1:
        return "Spock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "lizard"
    elif num == 4:
        return "scissors"


def rpsls(guess):
    player_number = name_to_number(guess)
    comp_number = random.randrange(0, 5)

    # print comp_number - player_number
    result = (comp_number - player_number) % 5  # NOTE: computer wins on 1 and 2; tie on 0; player wins otherwise

    print ""
    print "Player chooses " + number_to_name(player_number)
    print "Computer chooses " + number_to_name(comp_number)

    if result == 1 or result == 2:
        print "Computer wins!"
    elif result == 0:
        print "Tie!"
    else:
        print "Player wins!"
