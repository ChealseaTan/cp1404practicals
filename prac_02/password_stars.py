MINIMUM = 0


def main():
    """Get password to display stars."""
    password = get_password(MINIMUM)
    display_stars(password)


def display_stars(password):
    """Print the stars."""
    print(len(password) * "*")


def get_password(MINIMUM):
    """Validate input with error-checking."""
    password = input("Password: ")
    while len(password) <= MINIMUM:
        print("Invalid password")
        password = input("Password: ")
    return password


main()