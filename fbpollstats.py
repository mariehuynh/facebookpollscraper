from itertools import islice
from bs4 import BeautifulSoup
import mechanize
import secrets

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

url = 'http://www.facebook.com/login.php'
browser.open(url)
browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
browser.form['email'] = secrets.secretemail
browser.form['pass'] = secrets.secretpass
response = browser.submit()
#print response.read()

soup = BeautifulSoup(open('polldata.html'), 'html.parser')

#print(soup.prettify())

data = {}

# get full list of names from linked pages
results = soup.div.div
#for item in islice(soup.div.div.next_siblings, 5):
for item in soup.div.div.next_siblings:
  try:
    interest = item.find('div', '_3con').text.strip()
    print interest

    # link to names
    namelink = item.find('li', '_49cb').a['href']
    #print namelink
    
    # fetch names
    url = 'http://www.facebook.com' + namelink
    print url
    namepage = browser.open(url)
    namecontainer = BeautifulSoup(namepage.read(), 'html.parser').find('div', 'fbProfileBrowserList')

    # data[interest] = []
    # #print namecontainer
    # # Grab only the first text field with name, not how many friends in common
    # for namebox in namecontainer.find_all('div', 'fcb'):
    #   name = namebox.a.text
      
    #   data[interest].append(name)
      #print name

    data[interest] = [namebox.a.text for namebox in namecontainer.find_all('div', 'fcb')]

  except:
    pass



#Print statistics
for item, names in data.iteritems():
  print item + ": " + str(len(names))

# print data



