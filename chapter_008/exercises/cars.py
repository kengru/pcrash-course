# Exercise 8-14. Building a dictionary.

def make_car(make, car_type, **characteristics):
    car = {}
    car['make'] = make
    car['car_type'] = car_type
    for k, v in characteristics.items():
        car[k] = v
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
