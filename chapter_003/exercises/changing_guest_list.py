# Exercise 3-5. Removing people from the list.

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
