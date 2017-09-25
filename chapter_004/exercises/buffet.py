# Exercise 4-13. Creating and later rebuilding a tuple.

foods = ('pizza', 'ham', 'sandwich', 'beef', 'chicken')

print('The menu is:')
for food in foods:
    print(food.title())

foods = ('pizza', 'ham', 'sandwich', 'rice', 'beans')

print('The NEW menu is:')
for food in foods:
    print(food.title())
