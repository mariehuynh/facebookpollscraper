# facebookpollscraper
This fetches poll data (because the official API no longer supports it) and generates some stats based on it.  To use it, you'll need to put your login info into a secrets.py and download the page with the poll options.  As of this writing, it doesn't load properly when fetched via mechanize.  Facebook often changes things, so you may need to update the classes too.  Good luck.

This uses from itertools, BeautifulSoup, mechanize, logging, and collections.
