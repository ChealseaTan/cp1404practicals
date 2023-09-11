from prac_09.unreliable_car import UnreliableCar

my_car = UnreliableCar("Audi R8", 100, 50)
# print(my_car)
print(f"{my_car.name} drove {my_car.drive(20)}km, has {my_car.fuel} fuel left")
