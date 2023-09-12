from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""
current_taxi = None
total_bill = 0
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

print("Let's drive!")
print(MENU)
choice = input(">>> ").lower()

while choice != "q":
    if choice == "c":
        print("Taxis available:")
        for index, taxi in enumerate(taxis, 0):
            print(f"{index} - {taxi}")
        taxi_choice = int(input("Choose taxi: "))
        try:
            current_taxi = taxis[taxi_choice]
        except IndexError:
            print("Invalid taxi choice")
    elif choice == "d":
        if current_taxi is None:
            print("You need to choose a taxi before you drive")
        else:
            distance = int(input("Drive how far? "))
            current_taxi.start_fare()
            current_taxi.drive(distance)
            trip_cost = current_taxi.get_fare()
            total_bill += trip_cost
            print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    else:
        print("Invalid option")
    print(f"Bill to date: ${total_bill:.2f}")
    print(MENU)
    choice = input(">>> ").lower()
print(f"Bill to date: ${total_bill:.2f}")
print("Taxis are now:")
for index, taxi in enumerate(taxis, 0):
    print(f"{index} - {taxi}")



