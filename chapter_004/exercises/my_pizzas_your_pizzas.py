# Exercise 4-11. Copying lists.

pizzas = ['pepperoni', 'cheese', 'chicken', 'italian sausage']
friend_pizzas = pizzas[:]

pizzas.append('beef')
friend_pizzas.append('ice cream')

print('My favorite pizzas are:')
print(pizzas)

print("My friend's favorite pizza is:")
print(friend_pizzas)
