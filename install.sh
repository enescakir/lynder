#!/bin/sh
if hash youtube-dl 2>/dev/null; then
    echo "youtube-dl is already installed"
else
  echo "youtube-dl is not installed"
  echo "youtube-dl is installing now"
  brew install youtube-dl;
fi

if python3 -c "from bs4 import BeautifulSoup" 2>/dev/null; then
  echo "Beautiful Soup is already installed"
else
  echo "Beautiful Soup is not installed"
  echo "Beautiful Soup is installing now"
  pip3 install beautifulsoup4
fi

if python3 -c "import requests" 2>/dev/null; then
  echo "Requests is already installed"
else
  echo "Requests is not installed"
  echo "Requests is installing now"
  pip3 install requests
fi

chmod u+x lynder.py
cp lynder.py /usr/local/bin/lynder
echo "\n\033[92m  => lynder is installed globally. \033[0m\n"
