# SCORE MENU

from score import display_score_status

MENU = """(G)et a valid score
          (P)rint result 
          (S)how stars 
          (Q)uit"""


def main():

    score = get_score()
    print(MENU)
    choice = input("Your Choice = ").upper()

    while choice != 'Q':
        if choice == 'G':
            score = get_score()
        elif choice == "P":
            result = display_score_status(score)
            print("Result: ", result)
        elif choice == "S":
            display_stars(score)
        else:
            print("Invalid choice.")

        print('\n')
        print(MENU)
        choice = input("Your Choice = ").upper()

    print("Farewell :)")


def display_stars(score):
    for i in range(0, score):
        print('*', end=" ")


def get_score():
    score = int(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Invalid score. Must between 0 to 100.")
        score = int(input("Enter your score: "))
    return score


main()
