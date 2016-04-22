#This module holds my functions that manipulate files
import heapq
#This function comes from http://www.pataprogramming.com/2010/03/python-dict-n-largest/ with some modification
#With lots of help from https://docs.python.org/3.0/library/heapq.html
def largest(dictionary,numberwanted):
    return heapq.nlargest(numberwanted, dictionary, key = lambda k: dictionary[k])

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
            
#This function takes a filename and collumn number and prints the top five most frequent values and prints a horizontal bar chart representing their frequency.

def topFive(tarFile, colNum):
    with open(tarFile) as temp:
        workingFile = temp.readlines()
        table = []
        for line in workingFile:
            table.append(line.split(","))
    data = dict()
    for row in table:
     if row[colNum] not in data:
        data[row[colNum]] = 1
     else:
        data[row[colNum]] = data[row[colNum]] + 1   
    keys = largest(data,5)
    print("The top five most common names are")
    for item in keys:
        #This checks to see if the name is short, so that it can help align the bar chart.
        if (len(item) < 6):
            print(item + ": \t\t " + "*" * (data[item]))
        else:
            print(item + ": \t " + "*" * (data[item]))
            
#This Function returns the largest key/value pair in a dict built from a file.
def number1(tarFile, colNum):
    largest = None
    with open(tarFile) as temp:
        workingFile = temp.readlines()
        table = []
        for line in workingFile:
            table.append(line.split(","))
        data = dict()
    for row in table[1:]:
        if row[colNum] not in data:
            data[row[colNum]] = 1
        else:
            data[row[colNum]] = data[row[colNum]] + 1
    for currentVal in data.keys() :
        if largest is None or data[currentVal] > largest :
            largest = data[currentVal]
            key = currentVal
    print(key, largest)
    
#This function takes a target csv file, sums an entire collumn and averages its content.
def averageValue(tarFile, colNum):
    counter = 0
    total = 0
    with open(tarFile) as temp:
        workingFile = temp.readlines()
        table = []
        for line in workingFile:
            table.append(line.split(","))
    for row in table[1:]:
        counter = counter +1
        tempValue = row[colNum]
        tempValue = float(tempValue[1:])
        total = total + tempValue
    av = (total/counter)
    av = str(av)
    printAv = av[:5]
    return printAv    
        
#This function takes a target csv file, turns it into a table (list of lists), finds the largest value in one collumn of that list, then returns the value, and two other cells on that row
def topCustomer(tarFile, colNum):
    with open(tarFile) as temp:
        biggestAmount = None
        biggestRow = None
        rowNum = 0
        workingFile = temp.readlines()
        table = []
        for line in workingFile:
            table.append(line.split(","))
        for row in table[1:]:
            rowNum = rowNum + 1
            if biggestAmount is None or row[colNum] > biggestAmount:
                biggestAmount = row[colNum]
                biggestRow = rowNum
        # print(biggestAmount, biggestRow)
        print("The Best Customer is: ", table[biggestRow][1],table[biggestRow][2])
        print("They have paid: ", biggestAmount)
        print("$" * (int(float(biggestAmount[1:])/100)))
        print("Each '$' = 100 dollars")