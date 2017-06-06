## Lynder
Lynder is a tutorial downloader.
You can download whole lectures of course by one-command.
But able to download courses, you need to have Standard Lynda Account.
It's just 24.99$. It's worth every penny.

### Requirements
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  `pip3 install beautifulsoup4`
- [Requests](http://docs.python-requests.org/en/master/)
  `pip3 install requests`
- [youtube-dl](https://rg3.github.io/youtube-dl/)
  `brew install youtube-dl`

### Install
  `$ ./install.sh`
  It calls install commands of requirements.
  And it copies downloader to /usr/local/bin for calling globally.

### Folder Structure
```
- Tutorial Folder
---- CONTENT.md
---- OVERVIEW.md
---- 1 - Chapter A
-------- 1 - Topic A Video
-------- 1 - Topic A Transcript
-------- 2 - Topic B Video
-------- 2 - Topic B Transcript
-------- 3 - Topic C Video
-------- 3 - Topic C Transcript
---- 2 - Chapter B
-------- 1 - Topic D Video
-------- 1 - Topic D Transcript
-------- 2 - Topic E Video
-------- 2 - Topic E Transcript
-------- 3 - Topic F Video
-------- 3 - Topic F Transcript
---- 3 - Chapter C
---- Exercise Files
```

### Run
```bash
$ lynder.py

# Download a tutorial
$ lynder.py --url URL_OF_TUTORIAL
$ lynder.py -u URL_OF_TUTORIAL

# Download list of tutorials
# Links are seperated line by line in the txt
$ lynder.py --file list.txt
$ lynder.py -f list.txt
```
