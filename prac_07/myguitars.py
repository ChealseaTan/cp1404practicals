"""
The Client
Estimated Time: 35 mins
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


name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:.2f} added.")
    name = input("Name: ")

with open(FILENAME, "w") as out_file:
    for guitar in guitars:
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
