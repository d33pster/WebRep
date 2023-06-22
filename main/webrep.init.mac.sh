#!/bin/sh
clear
echo "Checking ... "
sleep 2

Dir='./output-files/'

if [ ! -d "$Dir" ]; then
  echo " "
  echo "Initializing first time setup ..."
  sleep 1
  echo "Initializing output directory ..."
  sleep 1
  mkdir output-files
fi

python3 -m pip install --upgrade pip
pip3 install requests
