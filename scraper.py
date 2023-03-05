import requests
from bs4 import BeautifulSoup

iron_blossom_url = "https://www.ironblosam.net/for_sale_by_owner.php"
website = requests.get(iron_blossom_url, timeout=5)

website.raise_for_status()

website_content = BeautifulSoup(website.content, 'html.parser')

week22 = website_content.select('table:-soup-contains("Week 22")')

print(week22)
