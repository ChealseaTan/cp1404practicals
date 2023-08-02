"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\ "


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if char.isupper():
            count_lower = 1
        elif char.islower():
            count_upper = 1
        elif char.isdigit():
            count_digit = 1

    # TODO: if any of the 'normal' counts are zero, return False
    if count_digit == 0 or count_upper == 0 or count_lower == 0:
        return False

    # TODO: if special characters are required, then check the count of those
    if SPECIAL_CHARS_REQUIRED:
        if char in SPECIAL_CHARACTERS:
            count_special = 1
        else:
            return False

    return True


main()

