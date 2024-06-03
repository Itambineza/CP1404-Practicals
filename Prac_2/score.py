"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = score_status(score)
    print(result)

    """generate a random score and print it's result"""

    random_score = random.uniform(0, 100)
    random_result = score_status(random_score)
    print(f"Random score: {random_score:.2f}")
    print(random_result)


def score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
