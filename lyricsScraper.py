
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









