import os
from pathlib import Path
images = os.listdir("./2012")

path = os.path.abspath("D:/Other/RS2012 Website/2012 Website/public/scss")

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

import requests
count = 0
base = "https://web.archive.org/"
for absPathFile in walkDirectory(path):
    linesRead = []
    linesWrite = []
    # string to search in file
    if(os.path.isfile(absPathFile)):
        with open(f'{absPathFile}', 'r') as fp:
            # read all lines using readline()

                linesRead = fp.readlines()
                for row in linesRead:
                    try:
                        if row.find(base) != -1:
                            after_base = row.split(base)[1]
                            index = 0
                            for i, c in enumerate(after_base):
                                if c == "\'" or c == ")" or c == "\"":
                                    index = i
                                    break

                            url = (base + after_base[:index])
                            r = requests.get(url, allow_redirects=True)

                            open('./2012/' + url.split("/")[-1], 'wb').write(r.content)
                            print(base + after_base[:index])
                            count +=1
                    except:
                        pass
print(f'count: {count}')
#from last '/' check image name