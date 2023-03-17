import os
images = os.listdir("./2012")

file = "world"
linesRead = []
linesWrite = []

# string to search in file
with open(f'{file}.hbs', 'r') as fp:
    # read all lines using readline()
    linesRead = fp.readlines()
    for row in linesRead:
        for image in images:
            if row.find(image) != -1:
                row = row.replace(row.split(image)[0].split("\"")[-1], "https://raw.githubusercontent.com/JesseGuerrero/web-files-darkan/master/2012/")
                print('line:', row, end="")
        linesWrite.append(row)
with open(f'{file}2.hbs', 'w') as fp:
    fp.writelines(linesWrite)