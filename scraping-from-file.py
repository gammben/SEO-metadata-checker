#import required libraries
import urllib2
from bs4 import BeautifulSoup

#import current date and show in a nice format
import time
import datetime
date = datetime.datetime.now().strftime("%y-%m-%d")


#function to encode parsed text
def encode(text):
    return text.encode('utf-8')

#open list of urls to parse
fhand = open("urlist.txt")

#open the document where info will be placed
fout = open('output.txt', 'a')

#loop that does the magic. Get, in order: URL, Title, Canonical, mobile alternate + Robots tag
for line in fhand: 
    line = line.rstrip()
    soup = BeautifulSoup(urllib2.urlopen(line))
    title1 = encode(soup.title.string)
    links = soup.findAll('link', rel='canonical')
    for link in links:
        canonical = encode(link['href'])
    alt = soup.find('link', rel="alternate", media="handheld")
    for link in links:
        try:
            alternate = encode(alt['href'])
        except:
            alternate = "no-alternate"
    findrobots = soup.find("meta", {"name":"robots"})
    for link in links:
        robots = encode(findrobots['content'])
    fout.write(line + ";" + title1 + ";"+  canonical + ";"+  alternate + ";"+  robots + ";"+  date + '\n')
    time.sleep(0.5)