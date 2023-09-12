from prac_09.silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Audi", 200, 2)

# print(fancy_taxi)
fancy_taxi.drive(18)
total_fare = fancy_taxi.get_fare()
print(f"{fancy_taxi}, total fare = {total_fare}")
