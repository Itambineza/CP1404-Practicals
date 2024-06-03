MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    score = get_valid_score()
    choice = input("Choice: ").upper()
    # importing the score status function from the score program we did before
    from score import score_status
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = score_status(score)
            print(f"Score: {score}, Result: {result}")
        elif choice == 'S':
            show_stars(score)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input("Choice: ").upper()

    print("Thank you. A bien to!")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100.")
        score = float(input("Score: "))
    return score


def show_stars(score):
    """Print stars equal to the score."""
    print('*' * int(score))


main()
