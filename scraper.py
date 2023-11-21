import requests
import argparse
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import os

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
    
    def send_email(self, week_num, to_email):
        msg = MIMEMultipart()
        msg['Subject'] = f"Updates to Iron Blossom Time Shares Week {week_num}"
        msg['From'] = os.environ['google_from_address']
        msg['To'] = to_email

        messageText = MIMEText(f'''Week {week_num} has had recent updates''','html')
        msg.attach(messageText)

        server = smtplib.SMTP('smtp.gmail.com:587') # smtp address and port
        server.ehlo('Gmail') # call this to start the connection
        server.starttls() # starts tls encryption. When we send our password it will be encrypted.
        server.login(os.environ['google_from_address'], os.environ['google_app_password'])
        server.sendmail(os.environ['google_from_address'], to_email, msg.as_string())
        server.quit()
    
def main():
    scraper = Scraper()

    parser = argparse.ArgumentParser()

    parser.add_argument("-wn", "--week_num", help="Week Number", type=int)
    parser.add_argument("-te", "--to_email", help="To Email")

    args = parser.parse_args()

    week_num = args.week_num
    if week_num == None:
        week_num = 22

    print(f"\nScraping Iron Blossom website for changes to week {week_num}\n")

    while True:
        try:
            website = scraper.send_request()
            current_content = scraper.get_week(week_num, website)

            time.sleep(3600)

            website = scraper.send_request()
            new_content = scraper.get_week(week_num, website)

            if new_content == current_content:
                continue
            else:
                print("Something has changed")
                scraper.send_email(week_num, args.to_email)
                continue

        except KeyboardInterrupt:
            print("\n\nQuitting Program\n")
            exit()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()