from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"Red")

print(car_1.make)
print(car_1.year)
print(car_1.model)
print(car_1.color)

print(car_2.make)
print(car_2.year)
print(car_2.model)
print(car_2.color)

car_1.drive()
car_1.stop()