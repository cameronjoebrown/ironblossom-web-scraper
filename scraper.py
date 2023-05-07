import requests
from bs4 import BeautifulSoup

class Scraper():
    # website = requests.get(self.get_url(), timeout=5)

    # website.raise_for_status()

    # website_content = BeautifulSoup(website.content, 'html.parser')

    # week22 = website_content.select('table:-soup-contains("Week 22")')

    def get_url():
        return "https://www.ironblosam.net/for_sale_by_owner.php"
