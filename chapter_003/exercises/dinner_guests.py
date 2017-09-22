# Exercise 3-9. Showing the amount of items in a list.

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

print('There are ' + str(len(people)) + ' people invited.')
