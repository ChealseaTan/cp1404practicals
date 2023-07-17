MINIMUM = 0


def main():
    password = get_password(MINIMUM)
    display_stars(password)


def display_stars(password):
    print(len(password) * "*")


def get_password(MINIMUM):
    password = input("Password: ")
    while password <= MINIMUM:
        print("Invalid password")
        password = input("Password: ")
    return password


main()
