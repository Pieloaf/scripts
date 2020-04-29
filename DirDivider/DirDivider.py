from os import listdir, mkdir, path
from shutil import copy2 
from math import ceil
from pprint import pprint

def getDirSize(dirPath):
    dirSize = path.getsize(dirPath)
    filesToMove = []
    for file in listdir(dirPath):
        if file[0] != '.' and file[:5] != 'Music':
            subDir = path.join(dirPath, file)
            filesToMove.append(subDir)
            dirSize += path.getsize(subDir)

    dirSize = dirSize*(10**-6)
    return (dirSize, filesToMove)

def divideDir(dstPath, files, limit):
    diskNum = 1
    dstPath = dstPath+'Disc'
    if limit < files[0]:
        limit = ceil(files[0]/2)

    for file in files[1]:
        dst = dstPath+str(diskNum)
        if not path.isdir(dst): mkdir(dst)

        if getDirSize(dst)[0] < limit:
            print(file)         
            copy2(file, dst)
        else:
            diskNum += 1
 
        

if __name__ == "__main__":

    maxDirSize = 700
    srcPath = '/Users/piercelowe/Music/'
    dstPath = '/Users/piercelowe/'
    
    x = getDirSize(srcPath)
    pprint(x[1])
    divideDir(dstPath, x, maxDirSize)


