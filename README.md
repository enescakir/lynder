## Lynder
> Lynda.com Tutorial Downloader

### Requirements
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  `pip3 install beautifulsoup4`
- [youtube-dl](https://rg3.github.io/youtube-dl/)
  `brew install youtube-dl`
- [Requests](http://docs.python-requests.org/en/master/)
  `pip3 install requests`

### Folder Structure
```
- Tutorial Folder
---- Content.md
---- Overview.md
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
```
./lynder.py
./lynder.py LINK_OF_TUTORIAL
```
