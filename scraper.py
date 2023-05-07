import requests
from bs4 import BeautifulSoup

class Scraper:
    

    # website.raise_for_status()

    # website_content = BeautifulSoup(website.content, 'html.parser')

    # week22 = website_content.select('table:-soup-contains("Week 22")')

    def get_url(self):
        return "https://www.ironblosam.net/for_sale_by_owner.php"

    def send_request(self):
        return requests.get(self.get_url(), timeout=5)