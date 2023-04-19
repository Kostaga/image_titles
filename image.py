import os
import re

rootdir = r"C:\Users\Konstaninos\Downloads\imagecompressor"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if (re.search("-min", file)):
            newfile = re.sub("-min", "", file)
            os.rename(f"{subdir}\{file}", f"{subdir}\{newfile}")
        if (re.search(" ", file)):
            newfile = re.sub(" ", "_", file)
            os.rename(f"{subdir}\{file}", f"{subdir}\{newfile}")

        if (re.search(r"[0-9]{3,4}", file)):
            res = re.search(r"[0-9]{3,4}", file)
            if (re.search(r".jpg", file)):
                period = re.search(".jpg", file)
            else:
                period = re.search(".JPG", file)
            path = subdir
            path = os.path.basename(path)
            name = os.path.basename(os.path.dirname(subdir))
            try:
                newfile = f"{name.lower()}_{file[res.start():period.start()]}.jpg"
                os.rename(f"{subdir}\{file}", f"{subdir}\{newfile}")
            except AttributeError:
                print("oi")

