"""
The Client
Estimated Time: 28 mins
Actual Time: 30 mins
"""

from prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append([name, year, cost])
    print(f"{name} ({year}) : ${cost:.2f} added.")
    name = input("Name: ")

name_width = max((len(guitar[0]) for guitar in guitars))
cost_width = max((len(f"{guitar[2]:,.2f}") for guitar in guitars))

print("These are my guitars: ")
for i, guitar in enumerate(guitars, 1):
    guitar_object = Guitar(guitar[0], guitar[1], guitar[2])
    if guitar_object.is_vintage():
        vintage_string = " (vintage)"
    else:
        vintage_string = ""
    print(f"Guitar {i}: {guitar[0]:>{name_width}} ({guitar[1]}), worth $ {guitar[2]:>{cost_width},.2f} {vintage_string}")

