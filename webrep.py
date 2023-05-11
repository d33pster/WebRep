#!/usr/bin/env python3
import subprocess
import requests
import time

#Checking and installing prereqs:
subprocess.call(['sh', './webrep.init.sh'])

#Functions:
def reader(file_name):
    file = open("./output-files/"+file_name+".rep", "r")
    print("\n")
    print(file.read())
    file.close()
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
            print("Fetching Report(s) ... ")
            time.sleep(3)
            print("\n")
            print("Saving into /output-files/"+output_file_name+".rep ...")
            time.sleep(2)
            for item, value in res.items():
                load_output_file = open("./output-files/"+output_file_name+".rep", "a")
                load_output_file.write(item+" : "+value+"\n\n")
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
        print("Fetching Report ...")
        time.sleep(2)
        print("\n")
        print("Saving into /output-files/"+output_file_name+".rep ...")
        time.sleep(2)
        for item, value in res.items():
            load_output_file = open("./output-files/"+output_file_name+".rep", "a")
            load_output_file.write(item+" : "+value+"\n\n")
            load_output_file.close()
    else:
        print("Invalid Input!")
        print("Restarting...")
        time.sleep(1)
        fetch()
    return
            
def main():
    print("\n\n")
    subprocess.call(['sh', './logo.sh'])
    decider = int(input("Press 1 to Diagnose :: Press 0 to browse existing report :: Press 10 to enter file-name: "))
    if(decider == 1):
        fetch()
        print("\n\nRECONFIGURING ...")
        time.sleep(2)
        main()
    elif(decider == 10):
        file_name = input("file-name: ")
        reader(file_name)
        code_choke = input("\n\n~ PRESS ENTER TO CONTINUE ~")
        print("\n\nRECONFIGURING ...")
        time.sleep(2)
        main()
    elif(decider == 0):
        print("\nThe Output Directory has the following files: ")
        subprocess.call(['sh', './browse.sh'])
        print("\n")
        file_name = input("file to read: ")
        reader(file_name)
        code_choke = input("\n\n~ PRESS ENTER TO CONTINUE ~")
        print("\n\nRECONFIGURING ...")
        time.sleep(2)
        main()
    else:
        print("Input Error! ~ Custom Exit Code 1")
        print("Restarting ...")
        time.sleep(2)
        main()
    return



#Driver:
main()