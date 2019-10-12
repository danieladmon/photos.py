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
#dir = "C:\\Users\DA\Desktop\motorcity"

deldir = os.path.join(dir,"del"); count = 0

if not os.path.exists(dir):
    print(f"Error: directory \"{dir}\" doesn't exist.")
    exit()

if not os.path.exists(deldir):
    os.makedirs(deldir)

for cr2 in os.listdir(dir):
    if cr2.endswith(".CR2"):
        jpg = os.path.join(dir,cr2.split(".")[0] + ".JPG")
        crfile = os.path.join(dir,cr2)
        if os.path.isfile(jpg) == False:
            delfile = os.path.join(deldir,cr2)
            if os.path.isfile(delfile)  == False:
                print(f"Moving file \"{crfile}\"")
                os.rename(crfile,delfile)
                count += 1
            else:
                print(f"Error: file \"{delfile}\" already exist.")

print(f"total moved: {count}")
