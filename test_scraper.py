import unittest
from scraper import Scraper

class TestScraper(unittest.TestCase):
    def test_get_url(self):
        url = 'https://www.ironblosam.net/for_sale_by_owner.php'
        result = Scraper.get_url()
        self.assertEqual(result, url);
        
if __name__ == '__main__':
    unittest.main()