from bs4 import BeautifulSoup
import requests
dumpert = 'https://www.dumpert.nl/'
r = requests.get(dumpert)
soup_file = r.text

soup = BeautifulSoup(soup_file, 'html.parser')
kudos = soup.find_all('section', attrs={'id': 'top5'})

print(type(kudos))
print(len(kudos))

#print(kudos.text)