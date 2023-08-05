"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Display the subject detail from data."""
    data = get_data()
    for detail in data:
        print(f"{detail[0]} is taught by {detail[1]} and has {detail[2]} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME, "r")
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


main()