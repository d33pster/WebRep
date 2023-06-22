#!/usr/bin/env python3

import subprocess
import os
import time
import initCheckMac

#Checking and installing prereqs:
initCheckMac.init_check()
import requests

directory = os.path.dirname(os.path.abspath(__file__)) #getting current dire /main
directory_outMain = os.path.dirname(directory) #getting dir after cd = /WebRep

def main():
  global directory, directory_outMain
  os.system("clear")
  #Logo
  
  os.chdir(directory)
  caller = subprocess.call(['sh', './logo.sh'])
  #Footprint
  print("Press Q to quit\n")
  url = input("Url: ")
  if(url.strip() == "Q" or url.strip() == "q"):
      os.system("clear")
      return
  output_file_name = input("output file-name: ")
  req_t = requests.get(url)
  req = dict(req_t.headers)

  
  os.chdir(directory_outMain)

  create_output_file = open(os.path.join(directory_outMain, "output-files", output_file_name+".rep"), "w")
  create_output_file.write("Footprint of "+url+" Webserver: \n\n")
  create_output_file.close

  print("Fetching Footprints ...")
  time.sleep(3)
  print("\n")
  print("Saving into /output-files/"+output_file_name+".rep ...")
  time.sleep(2)

  os.system("clear")

  for item, value in req.items():
      load_output_file = open(os.path.join(directory_outMain, "output-files", output_file_name+".rep"), "a")
      load_output_file.write(item+" : "+value+"\n\n")
      load_output_file.close()

  #Cookies
  cookies_t = requests.get(url).cookies
  cookies = tuple(cookies_t)

  load_output_file = open(os.path.join(directory_outMain, "output-files", output_file_name+".rep"), "a")
  load_output_file.write("\n\nCOOKIES: \n")
  load_output_file.close()

  for i in range(len(cookies)):
      load_output_file = open(os.path.join(directory_outMain, "output-files", output_file_name+".rep"), "a")
      load_output_file.write(str(cookies[i]))
      load_output_file.write("\n")
      load_output_file.close()

  #reader with code choke
  def reader(file_name):
      file = open(os.path.join(directory_outMain, "output-files", file_name+".rep"), "r")
      print("\n")
      print(file.read())
      file.close()
      code_choke = input("\n\n~ PRESS ENTER TO CONTINUE ~")
      return
    
  reader(output_file_name)

  print("\n\nRECONFIGURING ...")
  time.sleep(1.5)
  main()
  return

main()