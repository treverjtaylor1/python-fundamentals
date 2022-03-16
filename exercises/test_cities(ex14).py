#11-1 \ 11-2
import unittest

from exercise14 import city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        wichita_usa = city_country('wichita', 'usa')
        self.assertEqual(wichita_usa, 'wichita, Usa')

unittest.main()

