#This module holds my functions that manipulate files
def openFile(tarFile):
    with open(tarFile) as temp:
        fileDump = temp.readlines()
    return fileDump
    