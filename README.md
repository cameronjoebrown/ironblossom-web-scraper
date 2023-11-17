# Iron Blossom Web Scraper
A web scraper I'm making of the Iron Blossom Lodge Timeshares for Sale website ([see it here](https://www.ironblosam.net/for_sale_by_owner.php)) that notifies when a new Timeshare unit is posted for sale.

## How to Run
You'll need to have Python 3 with the following modules installed: requests and Beautiful Soup (bs4). Once you have those, run this:
```Shell
python scraper.py
```

It's currently hard coded to week 22, so you'll have to update that in scraper.py if you want a different week

The script will run until you end it with a standard KeyboardInterrupt (ctrl+c if running in standard terminal)