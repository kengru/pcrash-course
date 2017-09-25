# Slicing lists.

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'josh', 'alan']

print('Here are the last guys to come in: ')
for player in players[-3:]:
    print(player.title())
