# A dictionary in a dictionary.

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print('\nUsername: ' + username)
    print('\tFull name: ' + user_info['first'].title() + ' ' +
        user_info['last'].title())
    print('\tLocation: ' + user_info['location'].title())
