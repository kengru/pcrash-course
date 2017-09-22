# Modifying elements in lists.

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
del motorcycles[1]
print(motorcycles)

last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)
print(motorcycles)
print('The last motorcycle I owned was a ' + last_owned.title() + '.')
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
