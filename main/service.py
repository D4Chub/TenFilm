import requests
from bs4 import BeautifulSoup

url = 'https://hd.10rdfilmhd.online'


def get_soup():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('div', class_='th-item')
    for cards in data:
        link = cards.find('a', class_='th-in with-mask').get('href')
        image_link = url + cards.find('img').get('data-src')
        name = cards.find('div', class_='th-title').text
        rate = cards.find('div', class_='th-rate th-rate-kp').text
        print('--------------------------------')
        print(image_link, link, name, rate, sep='\n')


get_soup()