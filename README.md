# facebookpollscraper
This fetches poll data (because the official API no longer supports it) and generates some stats based on it.  To use it, you'll need to put your login info into a secrets.py and download the page with the poll options.  As of this writing, it doesn't load properly when fetched via mechanize so you'll just need to do it manually.  It does fetch the other pages with the lists of names of people who have voted for each option.  Facebook often changes things, so you may need to update the classes too.  This was also written for a specific problem so you'll have to tailor it to your needs.  Good luck.

## Requirements
This uses from itertools, BeautifulSoup, mechanize, logging, and collections.

## To Do
Generalize for other polls
Cleanup
Automate fetching of poll options
