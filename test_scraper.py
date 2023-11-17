import unittest
from unittest.mock import Mock, patch
from scraper import Scraper

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = Scraper()

    def test_should_get_url(self):
        url = 'https://www.ironblosam.net/for_sale_by_owner.php'
        result = self.scraper.get_url()
        self.assertEqual(result, url)

    def test_send_request_should_return_response(self):
        mock_response = Mock(status_code=200, json=Mock(return_value={"foo": "bar"}))
        with patch("requests.get", return_value=mock_response):
            result = self.scraper.send_request()
            self.assertEqual(result, mock_response)

if __name__ == '__main__':
    unittest.main()