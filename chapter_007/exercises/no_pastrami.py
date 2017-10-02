# Exercise 7-7. Removing word from list.

sandwich_orders = ['ham', 'pastrami', 'cheese', 'salami', 'pastrami', 'egg']
print(sandwich_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
