import requests
import time
from bs4 import BeautifulSoup

class Scraper:

    def get_url(self):
        return "https://www.ironblosam.net/for_sale_by_owner.php"

    def send_request(self):
        request = requests.get(self.get_url(), timeout=5)
        request.raise_for_status()
        return request
    
    def get_week(self, week_num, website):
        website_content = BeautifulSoup(website.content, 'html.parser')
        return website_content.select(f'table:-soup-contains("Week {week_num}")')
    
def main():
    scraper = Scraper()

    print("\nRunning\n")

    while True:
        try:
            website = scraper.send_request()
            current_content = scraper.get_week(22, website)

            time.sleep(3600)

            website = scraper.send_request()
            new_content = scraper.get_week(22, website)

            if new_content == current_content:
                continue
            else:
                print("Something has changed")
                continue
        except KeyboardInterrupt:
            print("\n\nQuitting Program\n")
            exit()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()