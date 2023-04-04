from bs4 import BeautifulSoup
import requests


html_text = requests.get('http://www.ilekarze.pl/forum/Fora-tematyczne/Zdrowie-kobiety/').text
f = open("html.txt", "w")
f.write(html_text)
f.close()
soup = BeautifulSoup(html_text, 'lxml')
topics = soup.find_all('td', 'td_post_tytul')
f = open("test.txt", "w")
for topic in topics:
    link = topic.find('a')
    titel = topic.find('a', 'a_text')
    print(titel.string)
    print(link.get('href'))
    f.write(titel.string + ' ')
    f.write(link.get('href') + '\n')
f.close()