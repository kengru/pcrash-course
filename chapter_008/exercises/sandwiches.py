# Exercise 8-12. Getting a list of items.

def sandwiches_order(*sandwiches):
    print('The sandwiches you ordered are:')
    for sandwich in sandwiches:
        print('* ' + sandwich)

sandwiches_order('ham', 'salami')
sandwiches_order('ham', 'egg', 'cheese')
sandwiches_order('extra cheese')
