# Exercise 11-1 and 11-2. Testing a simple function.

def format_city_country(city, country):
    return city.title() + ', ' + country.title()

def format_city_country_population(city, country, population):
    return city.title() + ', ' + country.title() + ' - Population: ' + str(population)
