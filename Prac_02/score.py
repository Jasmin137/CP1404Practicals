# BROKEN SCORE
import random


def main():
    score = int(input("Enter score: "))
    print(display_score_status(score))

    random_score = random.randint(0, 100)
    result = display_score_status(random_score)
    print(f"Random score: {random_score} and the result: {result}")


def display_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == 'main':
    main()
