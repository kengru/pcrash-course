# Exercise 10-10. Storing and reading from and to json.

import json

def get_favorite_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_favorite_number():
    number = input('What is your favorite number? ')
    filename = 'favorite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    return number

def get_number():
    number = get_favorite_number()
    if number:
        print('Your number is ' + number + '!')
    else:
        number = get_new_favorite_number()
        print('We will remember your number when you come back, ' +
              number + '!')

get_number()
