# Exercise 8-3. writing a function and handling arguments.

def make_shirt(size, message):
    print('Tshirt:')
    print('\tSize: ' + size)
    print('\tMessage: ' + message)

make_shirt('S', 'Nice shirt')
make_shirt(size='M', message='Inspirational message.')
