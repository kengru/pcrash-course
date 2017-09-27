# Exercise 6-4. Printing a dictionary with loops.

glossary = {
    'list': 'they store some information.',
    'dictionary': 'just like real life.',
    'for': 'go through a list or range.',
    'output': 'where something comes out.',
    'loop': 'repeats things.'
}

for k, v in glossary.items():
    print(k.title() + ': ' + v)
