import random

MIN_SCORE = 0
MAX_SCORE = 100

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Score menu program"""
    score = get_score()
    grade = get_grade()
    print(MENU)
    random_number = random.uniform(0, 100)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            student_score = get_score()
            print(score)
        elif choice == "P":
            student_score = validate_score(student_score)
            print(get_grade(student_score))
        elif choice == "S":
            student_score = validate_score(student_score)
            display_star((student_score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def get_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def validate_score(student_score):
    """Get a random score within the range"""
    if student_score == -1:
        student_score = get_score()
    return student_score


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
