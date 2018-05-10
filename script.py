from bs4 import BeautifulSoup
import requests
dumpert = 'https://www.dumpert.nl/'
r = requests.get(dumpert)
soup_file = r.text

soup = BeautifulSoup(soup_file, 'html.parser')
kudos = soup.find_all('section', attrs={'id': 'top5'})

#TODO
#Vind de juiste selector voor de top5 lijst, extract alle kudos
print(type(kudos))
print(len(kudos))

#print(kudos.text)