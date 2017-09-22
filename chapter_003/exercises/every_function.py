# Exercise 3-10. Using the functions on this chapter.

languages = []
languages.append('Spanish')
languages.insert(0, 'English')
languages.append('French')
languages.append('German')
print(languages)

print('The last language is ' + languages.pop() + '.')
languages.sort()
print('Sorted languages: ')
print(languages)
print('Reverted: ')
languages.reverse()
print(languages)
del languages[1]
languages.remove('Spanish')
print(languages)
