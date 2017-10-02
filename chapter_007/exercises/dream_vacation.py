# Exercise 7-8. Filling out a dictionary.

people_places = {}
not_done = True

while not_done:
    name = input('Who are you? ')
    place = input('Where? ')

    people_places[name] = place

    answer = input('Continue? (yes/no) ')
    if answer == 'no':
        not_done = False

for name, place in people_places.items():
    print(name.title() + ' likes ' + place.title() + '.')
