#import the library used to query a website
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
from bs4 import BeautifulSoup
import csv


finn = "https://m.finn.no/job/fulltime/search.html?industry=65&industry=8&location=1.20001.20012&filters="
page = urlopen(finn)
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())

divs = (soup.find_all('div', class_='result-item'))
titles = (soup.find_all('h3', class_='result-item-heading'))
jobs = []

for div in divs:
    for link in div.find_all('a'):
        results = []
        fulllink = 'https://m.finn.no' + link.get('href')
        results.append(fulllink)
        for title in link.find_all('p', class_='word-break'):
            results.append(title.get_text())
    jobs.append(results)
print(jobs)
outfile = open("./jobbs.csv", "w")
writer = csv.writer(outfile)
writer.writerows(jobs)