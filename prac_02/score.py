"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
MAXIMUM_VALUE = 100
MINIMUM_VALUE = 0
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50

score = float(input("Enter score: "))

if score > MAXIMUM_VALUE or score < MINIMUM_VALUE:
    print("Invalid score")
elif score >= EXCELLENT_THRESHOLD:
    print("Excellent")
elif score >= PASSABLE_THRESHOLD:
    print("Passable")
else:
    print("Bad")