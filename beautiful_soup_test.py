from bs4 import BeautifulSoup  # BeautifulSoup4 package
from urllib2 import urlopen

# Grab the HTML from a web page just like we did
# in the first example
my_address = "https://docs.python.org/2/whatsnew/2.7.html"
html_page = urlopen(my_address)
html_text = html_page.read()

# Pass the HTML to the BeautifulSoup constructor.
# The second argument tells beautifulsoup which parser to use
soup = BeautifulSoup(html_text, "lxml")
print soup.get_text().encode("utf-8")