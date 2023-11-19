# Iron Blossom Web Scraper
A web scraper I'm making of the Iron Blossom Lodge Timeshares for Sale website ([see it here](https://www.ironblosam.net/for_sale_by_owner.php)) that notifies when a new Timeshare unit is posted for sale.

## How to Run
You'll need to have Python 3 with the following modules installed: requests and Beautiful Soup (bs4). Once you have those, run this:
```Shell
python scraper.py
```

You'll also need the following environment variables:
```Shell
export google_app_password=<app_password> # you can create this from your google that you will use to send the email. it's free
export google_from_address=<email>
export to_email_address=<email>
```


It's currently hard coded to week 22, so you'll have to update that in scraper.py if you want a different week

The script will run until you end it with a standard KeyboardInterrupt (ctrl+c if running in standard terminal)