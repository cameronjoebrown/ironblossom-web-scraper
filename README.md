# Iron Blossom Web Scraper
A web scraper of the [Iron Blossom Lodge Timeshares for Sale website](https://www.ironblosam.net/for_sale_by_owner.php) that sends an email when a new Timeshare unit is posted for sale.

## How It Works
It checks for changes of week 22 postings. At the moment, this includes when postings are changed or removed.

## How to Run
You'll need to have Python 3 with the following modules installed: requests and Beautiful Soup (bs4). Once you have those, run this:
```Shell
python scraper.py -wn <week_num> -te <email_to_send_notifications_to> 
```

Example:
```Shell
python scraper.py -wn 22 -te example@gmail.com
```

You'll also need the following environment variables set:
```Shell
export google_app_password=<app_password> # you can create this from your google account that you will use to send the email. it's free
export google_from_address=<email>
```

The script will run until you end it with a standard KeyboardInterrupt (ctrl+c if running in standard terminal)

## Where To Run It
I have it running on a tmux session on a Raspberry Pi, but you could have it running on any server such as an EC2.