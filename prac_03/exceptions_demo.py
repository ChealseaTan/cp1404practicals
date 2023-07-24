"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when either the numerator or denominator is not an integer
2. When will a ZeroDivisionError occur?
when the denominator is a zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator can not be zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")