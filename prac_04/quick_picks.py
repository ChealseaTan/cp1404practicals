import random

tickets = []
numbers = []

MINIMUM_THRESHOLD = 1
MAXIMUM_THRESHOLD = 45
ROW = 6

line = int(input("Quick pick: "))

for loop in range(line):
    while len(numbers) < ROW:
        number = random.randint(MINIMUM_THRESHOLD, MAXIMUM_THRESHOLD)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    tickets.append(numbers)
    numbers = []

for ticket in tickets:
    for value in ticket:
        print(f"{value:2}", end=' ')
    print()
