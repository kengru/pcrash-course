# Exercise 7-4. Entering data and exit with a word.

prompt = 'Enter your pizza topping: '
message = ''

while message != 'quit':
    message = input(prompt)
    print(message.title() + ' topping!')
