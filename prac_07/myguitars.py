"""
The Client
Estimated Time:  mins
Actual Time: 45 mins
"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"

guitars = []
with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
    for i, line in enumerate(in_file, 0):
        name, year, cost = line.strip().split(",")
        guitars.append((Guitar(name, year, cost)))
        print(guitars[i])

guitars.sort()
print("\nSorted by year:")

for guitar in guitars:
    print(guitar)
