# Functions with a while loop.

def get_formatted_name(first_name, last_name):
    return (first_name + ' ' + last_name).title()

while True:
    print('\nPlease tell me your name: ')
    print('(enter q anytime to quit)')

    f_name = input('First name: ')
    if f_name == 'q':
        break

    l_name = input('Last name: ')
    if l_name == 'q':
        break

    print('\nHello ' + get_formatted_name(f_name,l_name) + '!')
