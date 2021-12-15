from playsound import playsound
import time, os

print("Welcome to the paxxous music creator, type ?help for more information.\n\n")



command = input()

if command == "?help":
  print("""
  
  Thank you for using pauxxs :D

  To create your first music file, type create, or crt

  to edit your first music file, type edit, or edt <Your file>

  To play your file, type play, or ply

  When in edit mode, type the order of notes that you would like to play, type intr({insert time here}) for an interval between notes.



  IMPORTANT:

  I only support the following notes:
  g, a, b, c, D, E, F, G

  (The high letters are high notes)

  look if you were looking to make a good song with this look elsewhere lol 
  """)

elif command == "easter":
  print("Shut up you're not getting an easter egg lol idiot")


elif command == "crt" or "create":
  nfile = open("Newfile", "a")
  



playsound(r"untitled.wav")
time.sleep(1)

print("My guy I just ended lmao")