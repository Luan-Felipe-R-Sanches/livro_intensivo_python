cars = ['bmw','audi','toyota','subaru']
cars.sort()
cars.sort(reverse=True)
print(cars)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original again:")
print(cars)

print(cars)

cars.reverse()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())