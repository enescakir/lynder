#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import os, sys, datetime, time
import requests
import argparse

def get_tutorial_data(link):
    tutorial = {}
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    tutorial["title"] = soup.find('h1', attrs={'class':'default-title'}).text.strip()
    tutorial["author"] = soup.find('cite', attrs={'data-ga-label':'author-name'}).text.strip()
    tutorial["download_at"] = datetime.datetime.now().strftime("%b %d, %Y")

    # toc = soup.find('ul', attrs={'class':'course-toc'})
    # for chapter in toc.find_all('li', attrs={'role':'presentation'}):
    #     ch = chapter.find('h4', attrs={'data-ga-label':'toc-chapter'})
    #     if ch:
    #         out.write("\n# "+ ch.text.strip() + "\n")
    #         print("# "+ ch.text.strip())
    #         for title in chapter.find_all('a', attrs={'class':'video-name'}):
    #             out.write("## " + title.text.strip()  + "\n")
    #             out.write(title["href"]  + "\n")
    #             print("## " + title.text.strip())

    return tutorial

if len(sys.argv) == 2:
    link = sys.argv[1]
else:
    link = input("Link of tutorial: ")
username = input("Lynda Username: ")
password = input("Lynda Password: ")

tutorial = get_tutorial_data(link)
print(tutorial)
