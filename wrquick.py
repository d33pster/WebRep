#!/usr/bin/env python3

import subprocess
import requests
import time
import initial_check

#Checking and installing prereqs:
initial_check.init_check()

def main():
  #Logo
  subprocess.call(['sh', './logo.sh'])

  #Footprint
  url = input("Url: ")
  output_file_name = input("output file-name: ")
  req_t = requests.get(url)
  req = dict(req_t.headers)

  create_output_file = open("./output-files/"+output_file_name+".rep", "w")
  create_output_file.write("Footprint of "+url+" Webserver: \n\n")
  create_output_file.close

  print("Fetching Footprints ...")
  time.sleep(3)
  print("\n")
  print("Saving into /output-files/"+output_file_name+".rep ...")
  time.sleep(2)

  for item, value in req.items():
      load_output_file = open("./output-files/"+output_file_name+".rep", "a")
      load_output_file.write(item+" : "+value+"\n\n")
      load_output_file.close()

  #Cookies
  cookies_t = requests.get(url).cookies
  cookies = tuple(cookies_t)

  load_output_file = open("./output-files/"+output_file_name+".rep", "a")
  load_output_file.write("\n\nCOOKIES: \n")
  load_output_file.close()

  for i in range(len(cookies)):
      load_output_file = open("./output-files/"+output_file_name+".rep", "a")
      load_output_file.write(str(cookies[i]))
      load_output_file.write("\n")
      load_output_file.close()

  #reader with code choke
  def reader(file_name):
      file = open("./output-files/"+file_name+".rep", "r")
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