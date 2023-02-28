# PASSWORD STARS

LENGTH = 6


def main():
    password = get_password()
    while len(password) < LENGTH:
        print("Password is short. Try again!")
        password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    return password


main()
