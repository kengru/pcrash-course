# Exercise 3-6. Adding people from the list.

people = ['Isaac Newton', 'Albert Einstein', 'Drake', 'LeBron James']

print('Hey, ' + people[0] + '. Can you come for dinner?')
print('Hey, ' + people[1] + '. Can you come for dinner?')
print('Hey, ' + people[2] + '. Can you come for dinner?')
print('Hey, ' + people[3] + '. Can you come for dinner?')

print(people.pop() + ' is not coming anymore :(')
people.append('Kanye West')

print('Hey, ' + people[0] + '. Can you come for dinner?')
print('Hey, ' + people[1] + '. Can you come for dinner?')
print('Hey, ' + people[2] + '. Can you come for dinner?')
print('Hey, ' + people[3] + '. Can you come for dinner?')

print('Found a bigger table, inviting more people.')

people.insert(0, 'Kevin Hart')
people.insert(2, 'Ray Allen')
people.append('Big Papi')

print('Hey, ' + people[0] + '. Can you come for dinner?')
print('Hey, ' + people[1] + '. Can you come for dinner?')
print('Hey, ' + people[2] + '. Can you come for dinner?')
print('Hey, ' + people[3] + '. Can you come for dinner?')
print('Hey, ' + people[4] + '. Can you come for dinner?')
print('Hey, ' + people[5] + '. Can you come for dinner?')
print('Hey, ' + people[6] + '. Can you come for dinner?')
