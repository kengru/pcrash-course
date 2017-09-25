# Exercise 5-9. Checking if list is not empty first.

usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello admin, would you like a status report?')
        else:
            print('Hello ' + user.title() + ' thank you for logging in again')
else:
    print('We need to find some users!')
