# Exercise 3-7. Removing some people off the list.

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

print(':((( I can now only invite 2 people :(((')

print('I am sorry ' + people.pop() + ', you are uninvited :(')
print('I am sorry ' + people.pop() + ', you are uninvited :(')
print('I am sorry ' + people.pop() + ', you are uninvited :(')
print('I am sorry ' + people.pop() + ', you are uninvited :(')
print('I am sorry ' + people.pop() + ', you are uninvited :(')

print('You are still uninvited ' + people[0] + ' ;)')
print('You are still uninvited ' + people[1] + ' ;)')

del people[1]
del people[0]

print(people)
