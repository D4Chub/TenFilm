import sqlite3

import requests
from bs4 import BeautifulSoup

url = 'https://hd.10rdfilmhd.online'

args = []


def get_soup():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('div', class_='th-item')
    for cards in data:
        link = cards.find('a', class_='th-in with-mask').get('href')
        image_link = url + cards.find('img').get('data-src')
        name = cards.find('div', class_='th-title').text
        rate = cards.find('div', class_='th-rate th-rate-kp').text[:3]
        category = cards.find('div', class_='')
        # print('--------------------------------')
        # print(image_link, link, name, rate, sep='\n')
        args.append((link, image_link, name, rate))

    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO movies VALUES (?, ?, ?, ?)", args)
    conn.commit()
    conn.close()


get_soup()