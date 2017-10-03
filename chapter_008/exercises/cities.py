# Exercise 8-5. Also using default function values.

def describe_city(city, country='Iceland'):
    print(city + ' is in ' + country + '.')

describe_city('Reykjavik')
describe_city('Iceisland')
describe_city('Santo Domingo', country='Dominican Republic')
