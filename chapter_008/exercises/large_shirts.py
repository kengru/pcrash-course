# Exercise 8-4. Using default arguments in function.

def make_shirt(size='L', message='I love Python'):
    print('Tshirt:')
    print('\tSize: ' + size)
    print('\tMessage: ' + message)

make_shirt()
make_shirt(size='M')
make_shirt('XXL', "Well, I'm big")
