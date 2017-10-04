# Exercise 8-9. Printing items from a list.

def show_magicians(magicians):
    for mage in magicians:
        print(mage.title())

mages = ['carl', 'johnny the guy', 'pearl the wonder', 'joe']
show_magicians(mages)
