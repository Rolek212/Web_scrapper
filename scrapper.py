from bs4 import BeautifulSoup
import requests

html_text = requests.get('http://www.ilekarze.pl/forum/Fora-tematyczne/Zdrowie-kobiety/').text
soup = BeautifulSoup(html_text, 'lxml')
topics = soup.find_all('')
print(html_text)