"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

MIN_SCORE = 0
MAX_SCORE = 100


def main():
    # score = float(input("Enter score: "))
    score = random.randint(MIN_SCORE, MAX_SCORE)
    return result_score(score)


def result_score(score):
    if 0 > score or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
    return score


main()
