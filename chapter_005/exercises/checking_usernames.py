# Exercise 5-10. Checking if a list's items are within another list.

current_users = ['peter', 'maria', 'john', 'admin', 'daniel']
new_users = ['Utal', 'Randy', 'Peter', 'maria', 'ramon']

for nuser in new_users:
    if nuser.lower() in current_users:
        print('You need to enter another username.')
    else:
        print('You can enter this username.')
