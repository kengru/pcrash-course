# Exercise 5-8. Looping a list and conditioning the results.

usernames = ['peter', 'maria', 'john', 'admin', 'daniel']
for user in usernames:
    if user == 'admin':
        print('Hello Admin, would you like a status report?')
    else:
        print('Hello ' + user.title() + ', thank you for logging in again')
