# Exercise 10-7. Adding 2 numbers and checking input repeatedly.

print('Enter [q] to quit.')

while True:
    try:
        number1 = input('First number: ')
        if number1 == 'q':
            break
        number2 = input('Second number: ')
        if number2 == 'q':
            break
        result = int(number1) + int(number2)
    except ValueError:
        print('Input is not a number.')
    else:
        print(result)
