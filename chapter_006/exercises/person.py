# Exercise 6-1. Storing information in a dictionary then accesing it.

edgar = {
    'first_name': 'Johnny',
    'last_name': 'Peterson',
    'age': 20,
    'city': 'Santo Domingo'
}

print('Hi, I am ' + edgar['first_name'] + ' ' + edgar['last_name'] +
    '. I am ' + str(edgar['age']) + ' years old and I live in ' +
    edgar['city'] + '.')
