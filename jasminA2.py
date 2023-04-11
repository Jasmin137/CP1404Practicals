import csv
import random

FILE_NAME = "a1.csv"


def main():
    print("Travel Tracker 1.0 - by Jasmin Kaur Kahlon")
    places = load_places()
    print(f"{len(places)} places loaded from {FILE_NAME}")

    while True:
        menu_choice = display_menu()
        if menu_choice == "l":
            display_places(places)
        elif menu_choice == "a":
            add_place(places)
        elif menu_choice == "m":
            mark_place(places)
        elif menu_choice == "r":
            recommend_place(places)
        elif menu_choice == "q":
            save_places(places)
            print(f"{len(places)} places saved to {FILE_NAME}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid choice. Please try again.")


def load_places():
    places = []
    try:
        with open(FILE_NAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                name, country, priority, visited = row
                places.append({"name": name, "country": country, "priority": int(priority), "visited": visited == "v"})
    except FileNotFoundError:
        pass
    return places


def save_places(places):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        for place in places:
            writer.writerow([place["name"], place["country"], place["priority"], "v" if place["visited"] else "n"])


def display_menu():
    print("\nMenu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("R - Recommend an unvisited place to visit")
    print("Q - Quit")
    return input(">>> ").lower()


def display_places(places):
    unvisited_places = [place for place in places if not place["visited"]]
    total_places = len(places)
    total_unvisited_places = len(unvisited_places)
    print(f"Total places: {total_places}")
    print(f"Unvisited places: {total_unvisited_places}")
    print(f"Visited places: {total_places - total_unvisited_places}")
    places.sort(key=lambda place: (place["visited"], -place["priority"], place["name"], place["country"]))
    name_width = max(len(place["name"]) for place in places)
    country_width = max(len(place["country"]) for place in places)
    for i, place in enumerate(places, 1):
        mark = "*" if not place["visited"] else " "
        print(f"{mark}{i}. {place['name']:<{name_width}} in {place['country']:<{country_width}} priority {place['priority']:>2}")


def add_place(places):
    name = input("Name: ")
    while not name:
        print("Input can not be blank")
        name = input("Name: ")
    country = input("Country: ")
    while not country:
        print("Input can not be blank")
        country = input("Country: ")
    priority = input("Priority: ")
    while not priority.isdigit():
        print("Invalid input; enter a valid number")
        priority = input("Priority: ")
    priority = int(priority)
    places.append({"name": name, "country": country, "priority": priority, "visited": False})
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")


def mark_place(places):
    """Mark a place as visited."""
    unvisited_places = [place for place in places if place[3] == 'n']
    if not unvisited_places:
        print("No unvisited places")
        return places
    else:
        print("Places to visit:")
        display_places(places)
        print()
        while True:
            try:
                index = int(input("Enter the number of a place to mark as visited: "))
                if index < 1 or index > len(places):
                    print(f"Please enter a number between 1 and {len(places)}")
                elif places[index-1][3] == 'v':
                    print(f"{places[index-1][0]} in {places[index-1][1]} has already been visited")
                else:
                    places[index-1][3] = 'v'
                    print(f"{places[index-1][0]} in {places[index-1][1]} marked as visited")
                    return places
            except ValueError:
                print("Please enter a valid number")


def recommend_place(places):
    """Recommend a random unvisited place."""
    unvisited_places = [place for place in places if place[3] == 'n']
    if len(unvisited_places) == 0:
        print("No places left to visit!")
    else:
        random_place = random.choice(unvisited_places)
        print(f"How about.....{random_place[0]} in {random_place[1]}?")


main()
