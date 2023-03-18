import os
from pathlib import Path
images = os.listdir("./2012")

path = os.path.abspath("D:/Other/RS2012 Website/2012 Website/public")

def walkDirectory(root):
    filePaths = list(Path(root).rglob("*"))
    result = []
    # for filePath in filePaths:
    #     if ".git" in str(filePath) or ".idea" in str(filePath) or "2012 Website\\bin" in str(filePath) \
    #             or "node_modules" in str(filePath) or ".scss" in str(filePath) or ".css" in str(filePath):
    #         continue
    for filePath in filePaths:
        if ".scss" in str(filePath):
            result.append(filePath)
    return result
count = 0
for absPathFile in walkDirectory(path):
    linesRead = []
    linesWrite = []
    # string to search in file
    if(os.path.isfile(absPathFile)):
        with open(f'{absPathFile}', 'r') as fp:
            # read all lines using readline()
            try:
                linesRead = fp.readlines()
                for row in linesRead:
                    for image in images:
                        if row.find("/" + image) != -1:
                            first_half = row.split(image)[0]
                            reversed_first_half = first_half[::-1]
                            splitter = "\""
                            for c in reversed_first_half:
                                if c == "\'":
                                    splitter = "\'"
                                    break
                                elif c == "(":
                                    splitter = "("
                                    break
                                elif c == "\"":
                                    break
                            row = row.replace(row.split(image)[0].split(splitter)[-1], "https://raw.githubusercontent.com/JesseGuerrero/web-files-darkan/master/2012/")
                            print(f'{absPathFile}, line:{row}', end="")
                            count +=1
                    linesWrite.append(row)
            except:
                pass
        with open(f'{absPathFile}', 'w') as fp:
            fp.writelines(linesWrite)
print(f'count: {count}')
#from last '/' check image name