# Exercise 10-2. Replacing a word on a file.

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    if 'python' in line:
        line = line.replace('python', 'c')
    print(line.strip())
