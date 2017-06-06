#!/bin/sh
pip3 install beautifulsoup4
pip3 install requests
brew install youtube-dl
chmod u+x lynder.py
cp lynder.py /usr/local/bin/lynder
echo "\033[92m  lynder is installed globally. \033[0m"
