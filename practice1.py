import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen('http://naver.com')

soup = BeautifulSoup(page, 'html.parser')

print(soup.find_all('p'))
print(soup.find('p'))
print(soup.find_all('p', class_='outer-text'))
print(soup.find_all(class_='outer-text'))
print(soup.find_all(id='outer-text'))

for tag in soup.find_all('p'):
    print(tag.get_text())

print(soup.prettify())