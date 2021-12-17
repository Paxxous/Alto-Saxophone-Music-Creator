from playsound import playsound
import time, os
playsound('audio/g.wav')


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
  g, a, b, c, D, E, F, F#, G

  (The high letters are high notes)

  look if you were looking to make a good song with this look elsewhere lol 
  """)

elif command == "easter":
  print("Shut up you're not getting an easter egg lol idiot")

elif command == "edt" or command == "edit":
  print("What file would you like to edit? (Make sure to add the .mcr file extension)")
  ofile = input()
  files = os.listdir()
  
  if ofile.startswith(tuple(files)):
    efile = open(ofile, "w")
    
    notes = input("Type your notes to play, (type a comma after a note, or else it could break the program.) Also make sure that you type notes that actually exist.\n")
    efile.write(notes)
    notes = notes.replace(',', '')
    lnotes = notes.split()
    


    print(lnotes)

    os.chdir('audio')



    for i in lnotes:
      
      print(i)
      
      playsound(i + '.wav')

    

    
  

elif command == "crt" or command == "create":
  nfile = open("Newfile.mcr", "a")
  print("Created file")
  





print("Ended program")
time.sleep(1)