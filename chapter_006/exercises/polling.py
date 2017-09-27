# Exercise 6-6. Condition to print while looping through a dictionary.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jack': 'c',
    'jose': ''
}

for k, v in favorite_languages.items():
    if v != '':
        print('Thank you, ' + k.title() + '.')
    else:
        print('Take the poll ' + k.title() + '!')
