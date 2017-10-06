# Exercise 10-1. Printing lines of a file.

filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
