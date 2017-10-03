# Exercise 8-7. Creating dictionaries on a function.

def make_album(artist, album_title, year=''):
    album = {}
    album['artist'] = artist
    album['title'] = album_title
    if year:
        album['year'] = year
    return album

print(make_album('John', 'Awaken', 1994))
print(make_album('Kaytranada', 'Got it good'))
print(make_album('Kanye', 'Beautiful'))
