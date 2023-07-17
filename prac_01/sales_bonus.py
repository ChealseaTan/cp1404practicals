"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_THRESHOLD = 1000
REGULAR_DISCOUNT = .1
ADDITIONAL_DISCOUNT = .15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < BONUS_THRESHOLD:
        bonus = sales * REGULAR_DISCOUNT
    else:
        bonus = sales * ADDITIONAL_DISCOUNT
    print(f"{bonus:.0f}")
    sales = float(input("Enter sales: $"))

