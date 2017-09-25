# Exercise 4-10. Using cubes, added some slicing operations to the list.

cubes = [number**3 for number in range(1,11)]
print(cubes)

print('First three items in the list:')
print(cubes[0:3])

print('Three items from the middle:')
print(cubes[4:7])

print('Last three items in the list:')
print(cubes[-3:])
