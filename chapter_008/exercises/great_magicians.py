# Exercise 8-10. Modifying a list from a function.

def make_great(magicians, great):
    while magicians:
        mage = magicians.pop()
        mage = 'The Great ' + mage + '!'
        great.append(mage)

def show_magicians(magicians):
    for mage in magicians:
        print(mage.title())

magicians = ['carl', 'johnny the guy', 'pearl the wonder', 'joe']
great = []
make_great(magicians, great)
show_magicians(great)
