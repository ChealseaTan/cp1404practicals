from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Display menu for taxi simulation."""
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxi(taxis)
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
                total_bill, trip_cost = calculate_fare(current_taxi, distance, total_bill)
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        else:
            print("Invalid option")
        display_total_bill(total_bill)
        print(MENU)
        choice = input(">>> ").lower()
    display_total_bill(total_bill)
    print("Taxis are now:")
    display_taxi(taxis)


def calculate_fare(current_taxi, distance, total_bill):
    current_taxi.start_fare()
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()
    total_bill += trip_cost
    return total_bill, trip_cost


def display_total_bill(total_bill):
    print(f"Bill to date: ${total_bill:.2f}")


def display_taxi(taxis):
    for index, taxi in enumerate(taxis, 0):
        print(f"{index} - {taxi}")


main()

