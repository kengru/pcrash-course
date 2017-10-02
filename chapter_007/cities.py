# Using break to exit a while loop.

prompt = '\nPlease enter the name of a city you have visited: '
prompt += '\n(Enter "quit" when you are finished.) '

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print('I would love to go to ' + city.title() + '!')
