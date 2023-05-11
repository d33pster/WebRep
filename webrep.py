#!/usr/bin/env python3

import platform
import time
import subprocess

P = platform.system()
def main():
  if(P == 'Linux'):
    print("Press 1 for quick :: Press 2 for default :: Press 0 to exit")
    dec = int(input(":: "))
    if(dec == 1):
        subprocess.call(['./wrquick_lin.py'])
    elif(dec == 2):
        subprocess.call(['./webrep_lin.py'])
    elif(dec == 0):
        return
    else:
        print("Invalid input!")
        print("\n")
        time.sleep(1)
        print("RECONFIGURING ...")
        time.sleep(2)
        main()
  elif(P == 'Windows'):
      print("Press 1 for quick :: Press 2 for default :: Press 0 to exit")
      dec = int(input(":: "))
      if(dec == 1):
          subprocess.call(['./win_redirect_quick.ps1'])  
      elif():
          subprocess.call(['./win_redirect.ps1'])
      elif(dec == 0):
          return
      else:
          print("Invalid Input!\n")
          time.sleep(1)
          print("RECONFIGURING ...")
          time.sleep(2)
          main()
  else:
      print("This Program does not Support this Operating System! :)")
  return
    
main()