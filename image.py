import os
import re

rootdir = r"C:\Users\Konstaninos\Downloads\imagecompressor"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if (re.search("-min",file)):
            newfile = re.sub("-min", "", file)
            os.rename(f"{subdir}\{file}",f"{subdir}\{newfile}")
        if (re.search(" ",file)):
            newfile = re.sub(" ", "_", file)
            os.rename(f"{subdir}\{file}", f"{subdir}\{newfile}")

        if (re.search("[0-9]{3,4}",file)):
            res = re.search("[0-9]{3,4}",file)
            period = re.search(".jpg",file)
            path = os.path.dirname(subdir)
            newfile = f"suite_{os.path.basename(path).lower()}_{file[res.start():period.start()]}.jpg"

            os.rename(f"{subdir}\{file}", f"{subdir}\{newfile}")