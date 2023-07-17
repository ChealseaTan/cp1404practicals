total_price = 0
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = .9

items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))

for loop in range(0, items, 1):
    price = float(input("Price of item: "))
    total_price += price

if total_price > DISCOUNT_THRESHOLD:
    total_price *= DISCOUNT_RATE
print(f"Total price for {items} items is ${total_price:.2f}")
