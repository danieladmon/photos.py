'''
photos.py by Daniel Admon

this script is made to make my life easier.
I'm a photographer that shout at RAW and JPEG.
why JPEG and RAW ? because its faster to view and organize photos with JPEG.
RAW is a large file and its slower then JPEG.
'''
import os

dir = "C:\\Users\DA\Desktop\motorcity"
deldir = dir + "\\del"
count = 0

if not os.path.exists(deldir):
    os.makedirs(deldir)

for f in os.listdir(dir):
    if os.path.splitext(f)[1] == ".CR2":
        fname = dir + "\\" + f.split(".")[0]+ ".JPG"
        if os.path.isfile(fname) == False:
            fpath = dir + '\\' + f
            if os.path.isfile(fpath):
                print(fname)
                os.rename(fpath,deldir + "\\" + f)
                count += 1
            else:
                print("file ",fname," already exist")

print("total moved: ",count)
