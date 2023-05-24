#!/usr/bin/env python3

import platform
import time
import subprocess
import os


P = platform.system()

def path_resolver(cwd):
    if(os.path.exists(cwd+"\\Desktop")):
        PROGPATH = cwd+"\\Desktop\\WebRep\\main\\windows.py"
    elif(os.path.exists(cwd+"\\OneDrive\\Desktop")):
        PROGPATH = cwd+"\\OneDrive\\Desktop\\Webrep\\main\\windows.py"
    else:
        print("Failed to Process Desktop Location..\n")
        PROGPATH = input("Enter Manually: (example: path\\to\\desktop\\Desktop)\n:: ")
        PROGPATH = PROGPATH + "\\WebRep\\main\\windows.py"
    return PROGPATH

def main():
  if(P == 'Linux'):
    print("Press 1 for quick :: Press 2 for default :: Press 0 to exit")
    dec = int(input(":: "))
    if(dec == 1):
        subprocess.call(['./main/wrquick_lin.py'])
    elif(dec == 2):
        subprocess.call(['./main/webrep_lin.py'])
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
      caller = subprocess.call("cls", shell=True)
      if(os.environ["HOMEPATH"] == os.getcwd()):
          PROGPATH = path_resolver(os.environ["HOMEPATH"])
      else:
            print("Are You already in the WEBREP directory?(y/n) ")
            choice = input(":: ")
            if(choice=="y" or choice=="Y"):
                PROGPATH = "main\\windows.py"
                if (os.path.exists(os.getcwd()+"\\output-files")==False):
                    print("Error in resolving directory path...\n Reconfiguring..")
                    time.sleep(1)
                    print("Reconfigure Successful ...")
                    time.sleep(1)
                    PROGPATH = path_resolver(os.environ["HOMEPATH"])
            elif(choice=="n" or choice=="N"):
                os.chdir(os.environ["HOMEPATH"])
                PROGPATH = path_resolver(os.getcwd())
            else:
                print("Invalid Input!\n")
                time.sleep(1)
                print("RECONFIGURING ...")
                time.sleep(2)
                main()
      print("Press 1 to RUN :: Press 0 to exit")
      dec = int(input(":: "))
      if(dec == 1):
          caller = subprocess.run(["python", PROGPATH], shell=True)
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