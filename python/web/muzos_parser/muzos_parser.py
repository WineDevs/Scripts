from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import download
import os,sys

os.chdir(sys.path[0])

site = requests.get('https://muzos.net/')

soup = BeautifulSoup(site.text,'lxml')

songs_count = 0

songs_links = []

for song in soup.find_all(class_='track-dl'):
    songs_count+=1

    songs_links.append(song['href'])

print('Founded '+str(songs_count)+' songs')

for link in songs_links:
    song_link = requests.get(link)
    
    soup = BeautifulSoup(song_link.text,'lxml')

    for dwn_link in soup.find_all('a',class_='btn fdl'):
        url = dwn_link['href']
        url_parse = urlparse(url)
        filename = os.path.basename(url_parse.path)
        try:
            download.download(url,'./songs/'+filename,replace=True)
        except RuntimeError:
            pass

    print('Parsed song!')