#!/bin/sh
if hash youtube-dl 2>/dev/null; then
    echo "youtube-dl is already installed";
else
  echo "youtube-dl is not installed";
  echo "youtube-dl is installing now";
  brew install youtube-dl
fi

python -c "import hdhdsf" 2>/dev/null
echo $?
pip3 install beautifulsoup4
pip3 install requests
chmod u+x lynder.py
cp lynder.py /usr/local/bin/lynder
echo "\033[92m  lynder is installed globally. \033[0m"
