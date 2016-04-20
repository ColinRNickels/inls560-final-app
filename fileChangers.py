#This module holds my functions that manipulate files
def openFile(tarFile):
    with open(tarFile) as temp:
        fileDump = temp.readlines()
    return fileDump
def percentBreakdown(tarFile, colNum):
    q1 = 0
    q2 = 0
    with open(tarFile) as temp:
        workingFile = temp.readlines()
        table = []
        for line in workingFile:
            table.append(line.split(","))
        for row in table:
            # print(row[colNum])
            # input()
            if row[colNum] == "Male":
                q1 = q1 + 1
            elif row[colNum] == "Female":
                q2 = q2 + 1
            else:
                continue
    print(q1,q2)
    input()
    p1 = (q1/(q1+q2)*100)
    print(p1)
    input()
    p2 = 100 - p1
    print(str(int(p1)) + " percent male")
    print(str(int(p2)) + " percent female")
            
        