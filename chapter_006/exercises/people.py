# Exercise 6-7. Some dictionaries within a list.

people = []

edgar = {
    'first_name': 'Johnny',
    'last_name': 'Peterson',
    'age': 20,
    'city': 'Santo Domingo'
}
susan = {
    'first_name': 'Susan',
    'last_name': 'Lawson',
    'age': 24,
    'city': 'Santo Domingo'
}
peter = {
    'first_name': 'Peter',
    'last_name': 'Johnson',
    'age': 41,
    'city': 'Bogota'
}
people.append(edgar)
people.append(susan)
people.append(peter)

for person in people:
    print('\nHi, I am ' + person['first_name'] + ' ' + person['last_name'] +
        '. I am ' + str(person['age']) + ' years old and I live in ' +
        person['city'] + '.')
