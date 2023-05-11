#!/bin/sh
echo "Checking ... "
sleep 2
sudo apt install python3-pip -y
python3 -m pip install --upgrade pip
pip3 install requests
