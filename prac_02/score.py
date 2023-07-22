import random

MAXIMUM_VALUE = 100
MINIMUM_VALUE = 0
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    """Get score to determine grade tier."""
    score = float(input("Enter score: "))
    result = give_grades(score)
    print(result)

    another_score = (random.randint(0, 100))
    print(another_score)
    another_result = give_grades(another_score)
    print(another_result)


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


main()
