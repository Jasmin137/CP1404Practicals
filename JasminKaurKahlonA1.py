# ASSIGNMENT 1

import random

# Constants
FILENAME = "a1.csv"


# Functions
def welcome_message():
    print("Travel Tracker 1.0 - by Jasmin Kaur Kahlon\n3 places loaded from a1.csv")


def display_menu():
    print("\nMENU")
    print("1. List all places")
    print("2. Recommend a place to visit")
    print("3. Add a new place")
    print("4. Mark a place as visited")
    print("5. Quit")


def load_places(filename):
    try:
        with open(filename, "r") as file:
            places = [line.strip().split(",") for line in file]
            for place in places:
                place[2] = int(place[2])
        return places
    except FileNotFoundError:
        return []


def save_places(places, filename):
    with open(filename, "w") as file:
        for place in places:
            file.write(",".join(str(p) for p in place) + "\n")


def display_places(places):
    print("\nLIST OF PLACES\n")
    unvisited_count = 0
    for place in places:
        if place[3] == "n":
            unvisited_count += 1
            print("{:<20} in  {:<20}  {:<20}  {}".format(place[0], place[1], place[2], "*"))
        else:
            print("{:<20} in {:<20}  {:<20}  {}".format(place[0], place[1], place[2], " "))
    print("Total number of places: {}".format(len(places)))
    print("Number of unvisited places: {}".format(unvisited_count))


def recommend_place(places):
    unvisited_places = [place for place in places if place[3] == "n"]
    if unvisited_places:
        place = random.choice(unvisited_places)
        print("\nYou should visit {} in {}".format(place[0], place[1]))
    else:
        print("\nNo places left to visit!")


def add_place(places):
    name = input("\nEnter the name of the new place: ")
    country = input("Enter the country of the new place: ")
    priority = None
    while not priority:
        try:
            priority = int(input("Enter the priority of the new place (1-5): "))
            if priority < 1 or priority > 5:
                print("Error: Priority must be between 1 and 5")
                priority = None
        except ValueError:
            print("Error: Priority must be an integer")
            priority = None
    places.append([name, country, priority, "n"])
    print("\n{} in {} (priority {}) has been added to the list of places".format(name, country, priority))


def mark_visited(places):
    # Check if there are unvisited places
    if not any(place["visited"] == "n" for place in places):
        print("No unvisited places.")
        return

    # Display the list of places
    display_places(places)

    # Prompt the user to select a place to mark as visited
    while True:
        choice = input("Enter the number of the place to mark as visited: ")

        # Check if the input is valid
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        index = int(choice) - 1

        if index < 0 or index >= len(places):
            print("Invalid input. Please enter a valid number.")
            continue

        if places[index]["visited"] == "v":
            print("That place has already been visited.")
            continue

        # Mark the place as visited
        places[index]["visited"] = "v"
        print(f"{places[index]['name']} in {places[index]['country']} marked as visited.")
        break


def main():
    # Load places from file
    places = load_places(FILENAME)

    # Welcome message
    welcome_message()

    while True:
        # Display menu and get user choice
        display_menu()
        choice = input(">>> ")
        if choice == 1:
            # List all places
            display_places(places)

        elif choice == 2:
            # Recommend an unvisited place
            recommend_place(places)

        elif choice == 3:
            # Add a new place
            add_place(places)

        elif choice == 4:
            # Mark a place as visited
            mark_visited(places)

        elif choice == 5:
            # Quit and save to file
            save_places(places, FILENAME)
            print("Thank you for using Travel Tracker! Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()
