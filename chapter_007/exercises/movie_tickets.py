# Exercise 7-5. Ifs on a loop.

age = ''
active = True

while active:
    age = int(input('Your age: '))
    if age < 3:
        print('Your ticket is free!')
    elif age >= 3 and age < 12:
        print('Your ticket costs $10!')
    else:
        print('Your ticket costs $15!')

    age = input('If you wanna leave, write quit: ')
    if age == 'quit':
        active = False
