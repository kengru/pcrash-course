# Exercise 10-9. Analyzing some texts.

filenames = ['stevenson.txt', 'theland.txt', 'womanwitts.txt']

for filename in filenames:
    try:
        count = 0
        with open(filename) as file_object:
            lines = file_object.readlines()
        for line in lines:
            count += line.lower().count('the')
        print(filename + ' has "the" ' + str(count) + ' times.')
    except FileNotFoundError:
        pass
