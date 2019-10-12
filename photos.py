import os
dir = "C:\\Users\DA\Desktop\motorcity"

for f in os.listdir(dir):
    if os.path.splitext(f)[1] == '.CR2':
        fname = dir + "\\" + f.split(".")[0]+ ".JPG"
        if os.path.isfile(fname) == False:
            print (fname)
            os.rename(dir + '\\' + f, dir + '\\del\\' +f)
