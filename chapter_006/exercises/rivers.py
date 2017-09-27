# Exercise 6-5. Looping dictionaries.

rivers = {
    'nile': 'egypt',
    'ozama': 'dr',
    'hudson': 'missouri'
}

for k, v in rivers.items():
    print('The ' + k.title() + ' river is in ' + v.title() + '.')

print('These rivers:')
for k in rivers.keys():
    print(k.title())
print('These places:')
for v in rivers.values():
    print(v.title())
