# TestCase for exercise 11-1 and 11-2.

import unittest
from city_functions import format_city_country
from city_functions import format_city_country_population

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        value = format_city_country('Santiago', 'chile')
        self.assertEqual(value, 'Santiago, Chile')

    def test_city_country_population(self):
        value = format_city_country_population('santiago', 'chile', 24445)
        self.assertEqual(value, 'Santiago, Chile - Population: 24445')

unittest.main()
