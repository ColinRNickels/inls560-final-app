#This module holds my functions that manipulate files
def openFile(tarFile):
    with open(tarFile) as temp:
        fileDump = temp.readlines()
    print("You opened " + tarFile)
    return fileDump

#This function takes a target file, and a collumn number of that file. It reads the file into a list of lists (a table.) and prints out a horizontal bar chart of the percentage breakdown of the two options for that collumn. This particular function is hard coded to look for Male and Female, but it could be changed to look for other values.
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
    p1 = (q1/(q1+q2)*100)
    p2 = 100 - p1
    print("*" * int((p1/10)) + " - " + str(int(p1)) + " percent male")
    print("*" * int((p2/10)) + " - " + str(int(p2)) + " percent female")
            
