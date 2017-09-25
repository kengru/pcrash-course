# Exercise 4-12. Printing full lists from old exercise.

my_foods = ['moro', 'pizza', 'aguacate']
friend_foods = my_foods[:]

my_foods.append('spaguetti')
friend_foods.append('chocolate')

print('My favorite foods are:')
for food in my_foods:
    print(food)

print('\nMy friends foods are:')
for food in friend_foods:
    print(food)
