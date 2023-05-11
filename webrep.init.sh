#!/bin/sh
echo "Checking ... "
sleep 2

Dir='./output-files/'

if [ ! -d "$Dir" ]; then
  echo " "
  echo "Initializing first time setup ..."
  sleep 1s
  echo "Initializing output directory ..."
  sleep 1s
  mkdir output-files
fi

sudo apt install python3-pip -y
python3 -m pip install --upgrade pip
pip3 install requests
