# Exercise 6-8. Dictionaries on a list.

pets = []

dog = {
    'name': 'john the dog',
    'owner': 'peter the human',
    'age': 4
}

cat = {
    'name': 'snag the cat',
    'owner': 'peter the human',
    'age': 2
}

horse = {
    'name': 'carnal the horse',
    'owner': 'peter the human',
    'age': 15
}

pets.append(dog)
pets.append(cat)
pets.append(horse)

for pet in pets:
    print(pet['name'].capitalize() + ', owned by: ' + pet['owner'].capitalize() +
    ' and is about: ' + str(pet['age']) + ' years old.')
