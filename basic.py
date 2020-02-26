import urllib.request
from bs4 import BeautifulSoup
import re  # regular expression

page = urllib.request.urlopen('http://naver.com')

soup = BeautifulSoup(page, 'html.parser')

print(soup.find_all('p'))
print(soup.find('p'))
print(soup.find('p', {'class': 'lime'}))
print(soup.find_all('p', class_='outer-text'))
print(soup.find_all(class_='outer-text'))
print(soup.find_all(id='outer-text'))
print(soup.find_all(id=re.compile("para$")))
print(soup.find_all(['title', 'p']))


for tag in soup.find_all('p'):
    print(tag.get_text())

tagsStartingWithB = soup.findAll(re.compile('^b'))
print([tag.name for tag in tagsStartingWithB])
