#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import os, sys, datetime, time
import requests
import argparse
from threading import Thread
import threading
from queue import Queue
import subprocess

HOME_DIR = os.getcwd()

def download_tutorial(link, username, password):
    os.chdir(HOME_DIR)
    tutorial = get_tutorial_data(link)
    create_folders(tutorial)
    create_overview_md(tutorial)
    create_content_md(tutorial)
    download_videos(tutorial, username, password)
    return tutorial

def get_tutorial_data(link):
    tutorial = {}
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    tutorial["title"] = soup.find('h1', attrs={'class':'default-title'}).text.strip()
    print("\n\"" + tutorial["title"] + "\" is found.")
    tutorial["author"] = soup.find('cite', attrs={'data-ga-label':'author-name'}).text.strip()
    tutorial["released_at"] = soup.find('span', attrs={'id':'release-date'}).text.strip()
    tutorial["time_required"] = soup.find('span', attrs={'itemprop':'timeRequired'}).text.strip()
    tutorial["description"] = soup.find('div', attrs={'itemprop':'description'}).text.strip()
    tutorial["level"] = soup.find('div', attrs={'class':'course-info-stat-cont'}).find('strong').text.strip()
    # tutorial["exercise_file"] = soup.find('section', attrs={'id':'tab-exercise-files'}).text or ""
    tutorial["subject_tags"] = [tag.text.strip() for tag in soup.findAll('a', attrs={'data-ga-label':'topic-tag'})]
    tutorial["software_tags"] = [tag.text.strip() for tag in soup.findAll('a', attrs={'data-ga-label':'software-tag'})]
    tutorial["downloaded_at"] = datetime.datetime.now().strftime("%b %d, %Y")

    chapters = {}
    toc = soup.find('ul', attrs={'class':'course-toc'})
    for index, chapter in enumerate(toc.find_all('li', attrs={'role':'presentation'})):
        ch = chapter.find('h4', attrs={'data-ga-label':'toc-chapter'})
        if ch:
            lectures = []
            for lecture in chapter.find_all('a', attrs={'class':'video-name'}):
                lectures.append((lecture.text.strip(), lecture["href"]))
            chapters[ch.text.strip().replace(":", " -").replace('/', "-")] = lectures

    tutorial["chapters"] = chapters
    print("\tIt has " + str(len(chapters)) + " chapters.")
    return tutorial

def create_folders(tutorial):
    os.mkdir(tutorial["title"])
    os.chdir(tutorial["title"])
    print("\t\"" + tutorial["title"] + "\" folder is created.")
    for chapter in tutorial["chapters"]:
        os.mkdir(chapter)
        print("\t\"" + chapter + "\" folder is created.")

def create_overview_md(tutorial):
    overview = open("OVERVIEW.md", "w")
    overview.write("**Title:** " + tutorial["title"] + "\n")
    overview.write("**Author:** " + tutorial["author"] + "\n")
    overview.write("**Released at:** " + tutorial["released_at"] + "\n")
    overview.write("**Downloaded at:** " + tutorial["downloaded_at"] + "\n")
    overview.write("**Time Required:** " + tutorial["time_required"] + "\n")
    overview.write("**Level:** " + tutorial["level"] + "\n")
    overview.write("**Subject Tags:** " + ', '.join(tutorial["subject_tags"]) + "\n")
    overview.write("**Software Tags:** " + ', '.join(tutorial["software_tags"]) + "\n")
    overview.write("**Description:** \n\t" + tutorial["description"] + "\n")
    overview.close()
    print("\tOVERVIEW.md is created.")

def create_content_md(tutorial):
    content = open("CONTENT.md", "w")
    content.write( "# "+ tutorial["title"] + " with " + tutorial["author"] + " on lynda.com \n")
    for chapter, lectures in tutorial["chapters"].items():
        content.write( "## " + chapter + "\n")
        for lecture in lectures:
            content.write( "### " + lecture[0] + "\n")
        content.write("\n")
    content.close()
    print("\tCONTENT.md is created.")

def download_videos(tutorial, username, password):
    for chapter, lectures in tutorial["chapters"].items():
        os.chdir(chapter)
        for index, lecture in enumerate(lectures):
            while(threading.activeCount() > WORKER_NUM):
                time.sleep(5)
            th = Thread(target=download_lecture, args=(lecture,index,))
            th.deamon = True
            th.start()
            th.join()

        os.chdir("..")
    print("DOWNLOADING IS DONE")
    os.system("open .")

def download_lecture(lecture, index):
    print("\n\t\"" + lecture[0] + "\" is downloading...")
    os.system("youtube-dl --output \"" + str(index + 1) + " - %(title)s.%(ext)s\" --username " + username + " --password " + password + " " + lecture[1] + " --write-sub --embed-subs")
    print("\t\"" + lecture[0] + "\" was downloaded.")

### MAIN METHOD
parser = argparse.ArgumentParser(description='Lynda Tutorial Downloader')
parser.add_argument('-u', '--url', dest="url", action='store')
parser.add_argument('-f', '--file', dest="file", action='store')
parser.add_argument('-w', '--worker', nargs=1, dest="worker", action='store')
arguments = parser.parse_args()

username = input("Lynda Username: ")
password = input("Lynda Password: ")

WORKER_NUM = 2

if arguments.worker:
    WORKER_NUM = int(arguments.worker[0])

print("Number of workers is: ", WORKER_NUM)

if arguments.file:
    urls = open(arguments.file,'r')
    for url in urls:
        download_tutorial(url.strip(), username, password)
else:
    if arguments.url:
        url = arguments.url
    else:
        url = input("URL of tutorial: ")
    download_tutorial(url, username, password)
