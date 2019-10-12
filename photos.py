'''
photos.py by Daniel Admon

this script is made to make my life easier.
I'm a photographer that shout at RAW and JPEG.
why JPEG and RAW ? because its faster to view and organize photos with JPEG.
RAW is a large file and its slower then JPEG.
'''
import os

dir = os.getcwd()
#dir = input("Please type path to the folder:  ")
deldir = dir + "\\del"; count = 0

if not os.path.exists(dir):
    print(f"Error: directory \"{dir}\" doesn't exist.")
    exit()

if not os.path.exists(deldir):
    os.makedirs(deldir)

for f in os.listdir(dir):
    if f.endswith(".CR2"):
        fname = dir + "\\" + f.split(".")[0] + ".JPG"
        if os.path.isfile(fname) == False:
            fpath = dir + '\\' + f
            if os.path.isfile(fpath):
                print(fname)
                os.rename(fpath,deldir + "\\" + f)
                count += 1
            else:
                print(f"Error: file \"{fname}\" already exist.")

print(f"total moved: {count}")
