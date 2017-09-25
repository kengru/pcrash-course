# Exercise 5-2. Creating diferent test conditions based on what was learned.

if 'ham' == 'ham' and 'ham' != 'cheese':
    print('Yes it does, ham.')

if 'ham' == 'HAM'.lower() or 'magic' != 'cool':
    print('Lower works.')

if 45 > 22:
    print('Math is on point.')

compilation = ['movies', 'tv', 'internet']

if 'movies' in compilation:
    print('Its here.')
if 'ipad' not in compilation:
    print('Yes, it is not here.')
