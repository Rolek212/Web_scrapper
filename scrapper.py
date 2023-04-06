from bs4 import BeautifulSoup
import requests
import csv

#main site
main_site = requests.get('http://www.ilekarze.pl/forum/').text
main_soup = BeautifulSoup(main_site, 'lxml')

#getting all forums
forums = main_soup.find('table', 'forum_table_lista_postow')
forum_links = forums.find_all('td', 'td_for_tytul')

#file
f = open("test.csv", "w")
writer = csv.writer(f)
writer.writerow(["Date", "Author", "Topic", "Content"])

for forum_link in forum_links:
    #link for single forum
    link = forum_link.find('a')
    
    #going to single forum
    forum_site = requests.get(link.get('href')).text
    forum_site = BeautifulSoup(forum_site, 'lxml')
    
    #extracting page numbers
    pages = forum_site.find('div', 'pagination')
    pages = pages.find_all('a')
   
    for i in range(1, int(pages[-2].text)+1):
        #going to another site of the post
        forum_site_sec = requests.get(link.get('href')+str(i)+'/').text
        forum_site_sec = BeautifulSoup(forum_site_sec, 'lxml')
        
        #getting all posts from site
        topics = forum_site_sec.find_all('td', 'td_post_tytul')
        
        
        for topic in topics:
            #link of single post
            post_link = topic.find('a')
            
            #going to single post
            site = requests.get(post_link.get('href')).text
            site = BeautifulSoup(site, 'lxml')
            
            #single post
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
#closing file
f.close()
