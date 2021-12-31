#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
#from datetime import date, time, timedelta
from shutil import make_archive
from zipfile import ZipFile

def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"): #checks if path exists
    # get the path to the file in the current directory
    src = path.realpath("textfile.txt")
    
    # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
    
    # copy over the permissions, modification times, and other info
    shutil.copy(src, dst) #Copies only the document content
    shutil.copystat(src, dst) #Copies even the metadata (Time etc)

    #This is to check the textfile.txt.bak metadata, You need to import datetime library
    #print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt.bak"))) 


    # rename the original file
    #os.rename("newfile.txt", "textfile.txt") #this renames the textfile

    # now put things into a ZIP archive
    root_dir, tail = path.split(src)
    shutil.make_archive("archive", "zip", root_dir) #makes zip file for entire directory


    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip", "w") as newzip:
      newzip.write("textfile.txt")
      newzip.write("textfile.txt.bak")
if __name__ == "__main__":
  main()
