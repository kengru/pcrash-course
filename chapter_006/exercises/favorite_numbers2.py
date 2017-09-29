# Exercise 6-10. Modified 6-2 to get multiple numbers.

phone = {
    'josh': [458456, 457778],
    'jack': [515488, 458777],
    'joseph': [445457, 454787],
    'max': [454877, 487782],
    'jose': [457787, 875115]
}

for k, v in phone.items():
    print(k.title() + ' numbers are: ')
    for value in v:
        print('\t' + str(value))
