# Exercise 7-6. Moving a list to another, one item at a time.

sandwich_orders = ['ham', 'cheese', 'salami', 'egg']
finished_sandwiches = []

while sandwich_orders:
    item = sandwich_orders.pop()

    print('Order done: ' + item.title())
    finished_sandwiches.append(item.title())

for sandwich in finished_sandwiches:
    print(sandwich)
