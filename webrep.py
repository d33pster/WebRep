#!/usr/bin/env python3

import platform
import time
import subprocess
import os

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
      caller = subprocess.call("cls", shell=True)
      PROGPATH = os.getcwd()+"\\Desktop\\WebRep"
      print("Press 1 for quick :: Press 2 for default :: Press 0 to exit")
      dec = int(input(":: "))
      if(dec == 1):
          CALLPATH_quick = " "
          if(os.path.exists(PROGPATH)):
              CALLPATH_quick = "python3 " + PROGPATH + "\\windows_q.py"
          else:
              CALLPATH_quic = os.getcwd() + "\\OneDrive\\Desktop\\WebRep\\windows_q.py"
              CALLPATH_quick = "python3 " + CALLPATH_quic
              if(os.path.exists(CALLPATH_quic)==False):
                  PROGPATH = input("Failed to Process Directory\n Enter Directory manually: ")
                  CALLPATH_quic = "python3 " + PROGPATH 
                  CALLPATH_quick = CALLPATH_quic + "\\windows_q.py"
          subprocess.run(CALLPATH_quick, shell=True)  
      elif(dec == 2):
          CALLPATH_def = " "
          if(os.path.exists(PROGPATH)):
              CALLPATH_def = "python3 " + PROGPATH + "\\windows.py"
          else:
              CALLPATH_d = os.getcwd() + "\\OneDrive\\Desktop\\WebRep\\windows.py"
              CALLPATH_def = "python3 " + CALLPATH_d
              if(os.path.exists(CALLPATH_d)==False):
                  PROGPATH = input("Failed to Process Directory\n Enter Directory manually: ")
                  CALLPATH_d = "python3 " + PROGPATH
                  CALLPATH_def = "python3 "+CALLPATH_d + "\\windows.py"
          subprocess.call(CALLPATH_def, shell=True)
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