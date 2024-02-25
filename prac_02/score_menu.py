import random

MIN_SCORE = 0
MAX_SCORE = 100

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Score menu program"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = validate_input()
            print(score)
        elif choice == "P":
            print(display_result(score))
        elif choice == "S":
            print(display_star(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def validate_input():
    """Get a random score within the range"""
    score = random.randint(MIN_SCORE, MAX_SCORE)
    return score


def display_result(score):
    """Determine the result based on score"""
    if 0 > score or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def display_star(score):
    """Display numbers of asterisks based on score"""
    return score * "*"


main()
