# Exercise 10-6. Adding 2 numbers and checking input.

number1 = input('First number: ')
number2 = input('Second number: ')

try:
    result = int(number1) + int(number2)
except ValueError:
    print('Input is not a number.')
else:
    print(result)
