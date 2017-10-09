# Exercise 10-3. Writing a file from input.

filename = 'guest.txt'
name = input('What is your name? ')

with open(filename, 'w') as file_object:
    file_object.write(name)
