import unittest
from scraper import city_halls
from scraper.scraper import Scraper


class ScraperTestCase(unittest.TestCase):

    def test_get_csv_file(self):
        self.assertTrue(Scraper().get_csv_file(city_halls.Tabatinga()))

if __name__ == '__main__':
    unittest.main()
