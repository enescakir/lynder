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
    tutorial["released_at"] = soup.find('span', attrs={'id':'release-date'}).text.strip()
    tutorial["time_required"] = soup.find('span', attrs={'itemprop':'timeRequired'}).text.strip()
    tutorial["description"] = soup.find('div', attrs={'itemprop':'description'}).text.strip()
    tutorial["level"] = soup.find('div', attrs={'class':'course-info-stat-cont'}).find('strong').text.strip()
    tutorial["exercise_file"] = soup.find('section', attrs={'id':'tab-exercise-files'}).text
    tutorial["subject_tags"] = [tag.text.strip() for tag in soup.findAll('a', attrs={'data-ga-label':'topic-tag'})]
    tutorial["software_tags"] = [tag.text.strip() for tag in soup.findAll('a', attrs={'data-ga-label':'software-tag'})]
    tutorial["download_at"] = datetime.datetime.now().strftime("%b %d, %Y")

    chapters = {}
    toc = soup.find('ul', attrs={'class':'course-toc'})
    for index, chapter in enumerate(toc.find_all('li', attrs={'role':'presentation'})):
        ch = chapter.find('h4', attrs={'data-ga-label':'toc-chapter'})
        if ch:
            lectures = []
            for lecture in chapter.find_all('a', attrs={'class':'video-name'}):
                lectures.append((lecture.text.strip(), lecture["href"]))
            chapters[ch.text.strip()] = lectures

    tutorial["chapters"] = chapters
    return tutorial

if len(sys.argv) == 2:
    link = sys.argv[1]
else:
    link = input("Link of tutorial: ")
username = input("Lynda Username: ")
password = input("Lynda Password: ")

tutorial = get_tutorial_data(link)
print(tutorial)
