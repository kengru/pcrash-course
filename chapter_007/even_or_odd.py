# The % operator. Gets reminder of division.

number = input('Enter a number, I\'ll say if it is even or odd: ')
number = int(number)

if number % 2 == 0:
    print('\nThe number ' + str(number) + ' is even.')
else:
    print('\nThe number ' + str(number) + ' is odd.')
