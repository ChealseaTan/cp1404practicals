"""
The Test
Estimated Time: 8 mins
Actual Time: 15 mins
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another guitar", 2013, 5000.50)

print(gibson)
print(another_guitar)

gibson_age = gibson.get_age()
print(gibson_age)  # 101
another_guitar_age = another_guitar.get_age()
print(another_guitar_age)  # 10

gibson_vintage = gibson.is_vintage()
print(gibson_vintage)  # True
another_guitar_vintage = another_guitar.is_vintage()
print(another_guitar_vintage)  # False
