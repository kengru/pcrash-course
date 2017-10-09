# Exercise 10-4. Taking inputs and putting them on a file.

filename = 'guest_book.txt'
done = True

with open(filename, 'a') as file_object:
    while done:
        names = input('[send "q" to exit] What is your name? ')
        if names != 'q':
            file_object.write(names + '\n')
        else:
            done = False
