# beautifulsoup library helps with webscraping
# using html of website to get information
# basic web scraping information
# example code that i will comment later
# this is to scrape from downloaded html - learn
# more to scrape from real websites
# with open('home.html', 'r') as html_file:
#   content = html_file.read()
#   parser method
#   soup =  BeautifulSoup(content, 'lxml')
#  // print(soup.prettify())
#   finds specific html tag given string, returns first one
#   tags = soup.find('h5')
#   tags = soup.find_all('h5')
#   for course in tags:
#       print(course.text) <-- prints only the text between the html tags
#   course_cards = soup.find_all('div', class_ = 'card)
#   for course in course_cards:
#      // print(course.h5) <--- grabs h5 tags inside div class cards
#       course_name = course.h5.text
#       course_price = course.a.text.split()[-1] <-- gets last element in the split
#       print(f'{course_name} costs {course_price}')


# scraping a real website!
# gets latest job apps from a job listing website
# requests information from website
# html_text = requests.get('').text <-- url to scrape
# soup = BeautifulSoup(html_text, 'lmxl')
# jobs = soup.find_all('li', class_  = [insert class name here])
# for index, job in enumerate(jobs):
#    job = soup.find('li', class_)
#    probably should use strip/trim method instead to keep words separated
#    company_name = job.find('h3', class_ = '').text.replace(' ', '')
#    skills = job.find('span', class_ = '').text.replace('  ', '')
#    job_published_date = job.find('span', class_ = '').span.text
#    more_info = job.header.h2.a['href']
# with open(f'posts/{index}.txt', 'w') as f:
#   f.write(company name.. etc)
# if 'few' in published_date:
# ^ doesnt belong right there but whatever its fine
# in main function
# while True:
# find_jobs()
# time.sleep(600) <-- every ten minutes

from bs4 import BeautifulSoup
import lxml
import time
import requests
import re
from urllib.request import urlopen

site_name = "http://azlyrics.com"
html_text = ""

def get_lyrics():
    print("Enter the name of the artist you would like to analyze: ")
    artist_name = input()
    artist_name = artist_name.replace(" ", "")
    name_chars = list(artist_name)
    base = site_name + "/" + name_chars[0] + "/" + artist_name + ".html"
    global html_text
    html_text = requests.get(base).text
    soup = BeautifulSoup(html_text, 'lxml')
    songs = soup.find_all("div", class_="listalbum-item")
    song_names = []
    song_links = []
    for song in songs:
        song_name = song.get_text()
        song_names.append(song_name)
        song_name = re.sub(r'\W+', '', song_name)
        song_name = song_name.replace(" ", "")
        song_name = song_name.lower()
        song_link = site_name + "/lyrics/" + artist_name + "/" + song_name + ".html"
        song_links.append(song_link)
    list_length = len(song_names)
    song_lyrics = []
    for i in range(list_length):
        print("Song name: " + song_names[i])
        print("Link: " + song_links[i])
        song_text = requests.get(song_links[i]).text
        soup_two = BeautifulSoup(urlopen(song_links[i]), 'lxml')
        temp = soup_two.find("div", class_ = False)
        lyrics = temp.find_next("div", class_ = False).get_text()
        song_lyrics.append(lyrics)
        print("Lyrics: " +lyrics)









