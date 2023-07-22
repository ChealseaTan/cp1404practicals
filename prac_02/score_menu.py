MAXIMUM_VALUE = 100
MINIMUM_VALUE = 0
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50
MENU = """(G)et a valid score (must be 0-100 inclusive)
        (P)rint result
        (S)how stars
        (Q)uit"""

def main():
    """Get score and use menu to determine what to do with the score."""
    score = get_valid_number("Score (0 - 100): ", MINIMUM_VALUE, MAXIMUM_VALUE)
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_number("Score (0 - 100): ", MINIMUM_VALUE, MAXIMUM_VALUE)
        elif choice == "P":
            result = give_grades(score)
            print(result)
        elif choice == "S":
            display_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input("Choice: ").upper()
    print("Farewell")


def give_grades(score):
    """Use score to determine grade tier."""
    if score > MAXIMUM_VALUE or score < MINIMUM_VALUE:
        result = "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        result = "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        result = "Passable"
    else:
        result = "Bad"
    return result

def get_valid_number(prompt, low, high):
    """Get valid input."""
    number = int(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = int(input(prompt))
    return number


def display_stars(star):
    """Print the stars."""
    print(star * "*")

main()
