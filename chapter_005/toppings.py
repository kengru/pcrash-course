# Using the not [!] operator.

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print('Adding ' + topping + '.')
    else:
        print('Sorry, we do not have ' + topping + '.')

print('\nFinished making your pizza!')
