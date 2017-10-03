# Exercise 8-8. User input to fill up a dictionary.

def make_album(artist, album_title):
    album = {}
    album['artist'] = artist
    album['title'] = album_title
    return album

while True:
    print('\nInsert your albums!')
    print('[insert q to quit]')

    arts = input('Artist: ')
    if arts == 'q':
        break
    albs = input('Album: ')
    if albs == 'q':
        break

    print(make_album(arts, albs))
