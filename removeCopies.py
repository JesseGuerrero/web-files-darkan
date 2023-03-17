import os, re
images = os.listdir("./2012")
path = os.path.abspath("./2012")

file = "world"
linesRead = []
linesWrite = []

for image in images:
    if re.search(r"\(\d\)", image) or " - Copy." in image:
        os.remove(os.path.join(path, image))