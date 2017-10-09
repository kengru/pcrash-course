# Exercise 10-5. While input to file.

filename = 'poll.txt'
done = True

with open(filename, 'a') as file_object:
    while done:
        names = input('[send "q" to exit] What is your name? ')
        poll = input('[send "q" to exit] What do you like about programming? ')
        if names != 'q' or poll != 'q':
            file_object.write(names + ': ' + poll + '.' + '\n')
        else:
            done = False
