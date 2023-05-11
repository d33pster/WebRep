#!/usr/bin/env python3
import subprocess
import requests
import time
import initial_check
import os

#Checking and installing prereqs:
initial_check.init_check()

#Functions:
def reader(file_name):
    file = open("./output-files/"+file_name+".rep", "r")
    print("\n")
    print(file.read())
    file.close()
    code_choke = input("\n\n~ PRESS ENTER TO CONTINUE ~")
    return


def fetch():
    print("\n\n")
    decider = int(input("Press 1 for URL file :: Press 0 to input manually: "))
    if(decider == 1):
        url_file = input("Enter absolute file-path: ")
        output_file_name = input("Enter Output file-name: ")
        create_output_file = open("./output-files/"+output_file_name+".rep", "w")
        urls = open(url_file, "r")
        for url in urls:
            url = url.strip()
            create_output_file.write("Footprint of "+url+" Webserver: \n\n")
            create_output_file.close()
            req = requests.get(url)
            res = dict(req.headers)
            print("Fetching Footprint(s) ... ")
            time.sleep(3)
            print("\n")
            print("Saving into /output-files/"+output_file_name+".rep ...")
            time.sleep(2)
            for item, value in res.items():
                load_output_file = open("./output-files/"+output_file_name+".rep", "a")
                load_output_file.write(item+" : "+value+"\n\n")
                load_output_file.close()
            cookies = tuple(req.cookies)
            load_output_file = open("./output-files/"+output_file_name+".rep", "a")
            load_output_file.write("\n\nCOOKIES: \n")
            load_output_file.close()
            for i in range(len(cookies)):
                load_output_file = open("./output-files/"+output_file_name+".rep", "a")
                load_output_file.write(str(cookies[i]))
                load_output_file.write("\n")
                load_output_file.close()
    elif(decider == 0):
        url = input("Enter URL: ")
        output_file_name = input("Enter Output file-name: ")
        create_output_file = open("./output-files/"+output_file_name+".rep", "w")
        url = url.strip()
        create_output_file.write("Footprint of "+url+" Webserver: \n\n")
        create_output_file.close()
        req = requests.get(url)
        res = dict(req.headers)
        print("Fetching Footprint ...")
        time.sleep(2)
        print("\n")
        print("Saving into /output-files/"+output_file_name+".rep ...")
        time.sleep(2)
        for item, value in res.items():
            load_output_file = open("./output-files/"+output_file_name+".rep", "a")
            load_output_file.write(item+" : "+value+"\n\n")
            load_output_file.close()
        cookies = tuple(req.cookies)
        load_output_file = open("./output-files/"+output_file_name+".rep", "a")
        load_output_file.write("\n\nCOOKIES: \n")
        load_output_file.close()
        for i in range(len(cookies)):
            load_output_file = open("./output-files/"+output_file_name+".rep", "a")
            load_output_file.write(str(cookies[i]))
            load_output_file.write("\n")
            load_output_file.close
    else:
        print("Invalid Input!")
        print("Restarting...")
        time.sleep(1)
        fetch()
    return output_file_name

def fetch_read(output_file_name):
    print("\n")
    decider = int(input("Press 1 to view Footprint :: press 0 to reconfigure: "))
    if(decider == 1):
        reader(output_file_name)
    elif(decider == 0):
        return
    return
            
def driver():
    print("\n\n")
    subprocess.call(['sh', './logo.sh'])
    decider = int(input("Press 1 to Diagnose :: Press 0 to browse existing report :: Press 10 to enter file-name: "))
    if(decider == 1):
        fetch_read_input = fetch()
        fetch_read(fetch_read_input)
        print("\n\nRECONFIGURING ...")
        time.sleep(2)
        driver()
    elif(decider == 10):
        file_name = input("file-name: ")
        reader(file_name)
        print("\n\nRECONFIGURING ...")
        time.sleep(2)
        driver()
    elif(decider == 0):
        print("\nThe Output Directory has the following files: ")
        subprocess.call(['sh', './browse.sh'])
        print("\n")
        file_name = input("file to read: ")
        if (os.path.exists(os.path.join(os.getcwd(),"output-files/"+file_name+".rep")) == False):
            print("File Not Found! ")
            time.sleep(1)
            print("\nRECONFIGGURING ...")
            time.sleep(2)
            driver()
        else:
            reader(file_name)
            print("\n\nRECONFIGURING ...")
            time.sleep(2)
            driver()
    else:
        print("Input Error! ~ Custom Exit Code 1")
        print("Restarting ...")
        time.sleep(2)
        driver()
    return



#Driver:
driver()