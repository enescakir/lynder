#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import os, sys, datetime, time
import requests

response = requests.get(sys.argv[1])
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find('h1', attrs={'class':'default-title'}).text.strip()
author = soup.find('cite', attrs={'data-ga-label':'author-name'}).text.strip()
date = datetime.datetime.now().strftime("%b %d, %Y")
out = open(title + ".txt", "w")
out.write("\t" + title + " with " + author + " on lynda.com at " + date + "\n\n")
print("\t" + title + " with " + author + " on lynda.com at " + date)
out.write("→")
print("→\n")
toc = soup.find('ul', attrs={'class':'course-toc'})
for chapter in toc.find_all('li', attrs={'role':'presentation'}):
    ch = chapter.find('h4', attrs={'data-ga-label':'toc-chapter'})
    if ch:
        out.write("\n# "+ ch.text.strip() + "\n")
        print("# "+ ch.text.strip())
        for title in chapter.find_all('a', attrs={'class':'video-name'}):
            out.write("## " + title.text.strip()  + "\n")
            out.write(title["href"]  + "\n")
            print("## " + title.text.strip())

out.close()
