# Exercise 6-9. Dictionaries in a dictionaries.

favorite_places = {
    'john': {
        'paris',
        'rome'
    },
    'marie': {
        'london',
        'berlin'
    }
}

for k, v in favorite_places.items():
    print(k.title() + ' likes:')
    for value in v:
        print('\t' + value.title())
