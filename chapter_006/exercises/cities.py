# Exercise 6-11. Printing info from a dictionary.

cities = {
    'London': {
        'Country': 'UK',
        'Population': '2450000',
        'Fact': 'There is polution here.'
    },
    'Santo Domingo': {
        'Country': 'Dominican Republic',
        'Population': '1200000',
        'Fact': 'Tons of traffic.'
    },
    'Lima': {
        'Country': 'Peru',
        'Population': '500000',
        'Fact': 'High above the sea.'
    }
}

for key in cities.keys():
    print('Facts about ' + key + ':')
    for k, v in cities[key].items():
        print('\t' + k + ': ' + v)
