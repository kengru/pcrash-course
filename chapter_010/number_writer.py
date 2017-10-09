# Writing data into a json.

import json

numbers = [2, 3, 5, 6, 8, 23, 44]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
