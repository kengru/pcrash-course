# Exercise 10-8 Creating files then reading them.

with open('cats.txt', 'w') as file_object:
    file_object.write('Gato1')
    file_object.write('Gato2')
    file_object.write('Pedro')

with open('dogs.txt', 'w') as file_object:
    file_object.write('Perro1')
    file_object.write('Perro1')
    file_object.write('German')

try:
    with open('cats.txt') as file_object:
        print(file_object.read().strip())
    with open('dogs.txt') as file_object:
        print(file_object.read().strip())
except FileNotFoundError:
    pass
