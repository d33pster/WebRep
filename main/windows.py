#!/usr/bin/env python
import subprocess
import time
import os

# Checking and installing prereqs:
print("Checking ...\n")
caller = subprocess.run(["python.exe", "-m", "pip", "install", "--upgrade", "pip"], shell=True)
caller = subprocess.run(["pip", "install", "requests"], shell=True)
print("\n\n")
ch_dir = os.path.join(os.environ["HOMEPATH"], "Desktop\\WebRep")
if os.path.exists(ch_dir):
    if not os.path.exists(ch_dir + "\\output-files"):
        caller = subprocess.run(["cd", "Desktop\\webrep"], shell=True)
        os.chdir(ch_dir)
        os.mkdir("output-files")
    caller = subprocess.run(["Git", "-C", ch_dir, "pull", "https://www.github.com/d33pster/WebRep.git"], shell=True)
elif not os.path.exists(ch_dir):
    ch_dir = os.path.join(os.environ["HOMEPATH"], "OneDrive\\Desktop\\WebRep")
    if not os.path.exists(ch_dir + "\\output-files"):
        caller = subprocess.run(["cd", "onedrive\\desktop\\webrep"], shell=True)
        os.chdir(ch_dir)
        os.mkdir("output-files")
    caller = subprocess.run(["Git", "-C", ch_dir, "pull", "https://www.github.com/d33pster/WebRep.git"], shell=True)
else:
    print("Cannot Resolve Desktop Path ... \n")
    ch_dir = input("Enter Path to Desktop: (example: path\\to\\desktop\\Desktop)")
    ch_dir = os.path.join(ch_dir, "\\WebRep")
    if not os.path.exists(ch_dir + "\\output-files"):
        caller = subprocess.run(["cd", ch_dir], shell=True)
        os.chdir(ch_dir)
        os.mkdir("output-files")

    caller = subprocess.run(["Git", "pull", "https://www.github.com/d33pster/WebRep.git"], shell=True)

import requests


# Functions:

def reader(file_name):
    caller = subprocess.run("cls", shell=True)
    file = open(ch_dir + "\\output-files\\" + file_name + ".rep", "r")
    print(file.read())
    file.close()
    code_choke = input("\n\n~ PRESS ENTER TO CONTINUE ~")
    return


def fetch():
    global output_file_name
    print("\n\n")
    decider = int(input("Press 1 for URL file :: Press 0 to input manually: "))
    if decider == 1:
        url_file = input("Enter absolute file-path: ")
        output_file_name = input("Enter Output file-name: ")
        create_output_file = open(ch_dir + "\\output-files\\" + output_file_name + ".rep", "w")
        urls = open(url_file, "r")
        for url in urls:
            url = url.strip()
            create_output_file.write("Footprint of " + url + " Webserver: \n\n")
            create_output_file.close()
            req = requests.get(url)
            res = dict(req.headers)
            print("Fetching Footprint(s) ... ")
            time.sleep(3)
            print("\n")
            print("Saving into ...\\output-files\\" + output_file_name + ".rep ...")
            time.sleep(2)
            for item, value in res.items():
                load_output_file = open(ch_dir + "\\output-files\\" + output_file_name + ".rep", "a")
                load_output_file.write(item + " : " + value + "\n\n")
                load_output_file.close()
            cookies = tuple(req.cookies)
            load_output_file = open(ch_dir + "\\output-files\\" + output_file_name + ".rep", "a")
            load_output_file.write("\n\nCOOKIES: \n")
            load_output_file.close()
            for i in range(len(cookies)):
                load_output_file = open(ch_dir + "\\output-files\\" + output_file_name + ".rep", "a")
                load_output_file.write(str(cookies[i]))
                load_output_file.write("\n")
                load_output_file.close()
    elif decider == 0:
        url = input("Enter URL: ")
        output_file_name = input("Enter Output file-name: ")
        create_output_file = open(ch_dir + "\\output-files\\" + output_file_name + ".rep", "w")
        url = url.strip()
        create_output_file.write("Footprint of " + url + " Webserver: \n\n")
        create_output_file.close()
        req = requests.get(url)
        res = dict(req.headers)
        print("Fetching Footprint ...")
        time.sleep(2)
        print("\n")
        print("Saving into ...\\output-files\\" + output_file_name + ".rep ...")
        time.sleep(2)
        for item, value in res.items():
            load_output_file = open(ch_dir + "\\output-files\\" + output_file_name + ".rep", "a")
            load_output_file.write(item + " : " + value + "\n\n")
            load_output_file.close()
        cookies = tuple(req.cookies)
        load_output_file = open(ch_dir + "\\output-files\\" + output_file_name + ".rep", "a")
        load_output_file.write("\n\nCOOKIES: \n")
        load_output_file.close()
        for i in range(len(cookies)):
            load_output_file = open(ch_dir + "\\output-files\\" + output_file_name + ".rep", "a")
            load_output_file.write(str(cookies[i]))
            load_output_file.write("\n")
            load_output_file.close()
    else:
        print("Invalid Input!")
        print("Restarting...")
        time.sleep(1)
        fetch()
    return output_file_name


def fetch_read(output_filename):
    print("\n")
    decider = int(input("Press 1 to view Footprint :: press 0 to reconfigure: "))
    if decider == 1:
        reader(output_filename)
    elif decider == 0:
        return
    return


def driver():
    print("\n")
    caller = subprocess.run("cls", shell=True)
    logo = open(ch_dir + "\\main\\logo.txt", "r")
    print(logo.readline())
    logo.close()
    print("\n")
    print("Press 1 to Diagnose :: Press 2 to browse existing report ")
    print("Press 00 to EXIT")
    decider = int(input(":: "))
    if decider == 1:
        fetch_read_input = fetch()
        fetch_read(fetch_read_input)
        print("\n\nRECONFIGURING ...")
        time.sleep(2)
        driver()
    elif decider == 2:
        print("\nThe Output Directory has the following files: ")
        caller = subprocess.run(["cd", ch_dir + "\\output-files", "&", "dir"], shell=True)
        print("\n")
        file_name = input("file to read: ")
        if not os.path.exists(ch_dir + "\\output-files\\" + file_name + ".rep"):
            print("File Not Found! ")
            time.sleep(1)
            print("\nRECONFIGURING ...")
            time.sleep(2)
            driver()
        else:
            reader(file_name)
            print("\n\nRECONFIGURING ...")
            time.sleep(2)
            driver()
    elif decider == 0:
        return
    else:
        print("Input Error! ~ Custom Exit Code 1")
        print("Restarting ...")
        time.sleep(2)
        driver()
    return


# Driver:
driver()
