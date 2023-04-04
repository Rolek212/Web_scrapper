from bs4 import BeautifulSoup
import requests
import csv

#main site
html_text = requests.get('http://www.ilekarze.pl/forum/Fora-tematyczne/Zdrowie-kobiety/').text

#searching for posts
soup = BeautifulSoup(html_text, 'lxml')
topics = soup.find_all('td', 'td_post_tytul')

#file
f = open("test.csv", "w")
writer = csv.writer(f)
writer.writerow(["Date", "Author", "Topic", "Content"])

for topic in topics:
    link = topic.find('a')
    
    #going to single post
    site = requests.get(link.get('href')).text
    site = BeautifulSoup(site, 'lxml')
    
    #post
    post = site.find('div', 'forum_post')
    
    #date of the post
    date = post.find_all('p')
    date = date[-1].text
    
    #author of the post
    author = post.find('p')
    author = author.find('a').text
    
    #title of the post
    title = post.find('h2').text
    
    #content of the post
    post_content = site.find('div', 'tresc_posta').text
    
    #removing unnecessary content
    post_content = post_content.replace('Udostępnij', '')
    post_content = post_content.replace(' » Link do posta » Zgłoś do moderacji', '')
    post_content = post_content.strip()

    #writing to file
    writer.writerow([date, author, title, post_content])

f.close()

#testing space(to be deleted)
'''
#site = requests.get('http://www.ilekarze.pl/forum/Fora-tematyczne/Zdrowie-kobiety/mleko-modyfikowane-1666903947.html').text
site = requests.get('http://www.ilekarze.pl/forum/Fora-tematyczne/Zdrowie-kobiety/objawy-menopauzy.html').text
soup2 = BeautifulSoup(site, 'lxml')
post = soup2.find('div', 'forum_post')
date = post.find('h2').text
#date = date.find('a').text
f = open('oi.txt', 'w')
#f.write(str(post))
#f.write(author + ' ')
f.write(date)
f.close()
'''