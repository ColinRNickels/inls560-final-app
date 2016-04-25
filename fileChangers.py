#This module holds my functions that manipulate files
import urllib.request, urllib.error
import heapq

#This function comes from http://www.pataprogramming.com/2010/03/python-dict-n-largest/ with some modification
#My understanding of Heaps is limited, but they seem like a good way to store different kinds of data in a sortable data structure. And they have built in functions that return the largest values.
#With lots of help from https://docs.python.org/3.0/library/heapq.html
#In the below, Lamba serves to create an anonymous function that basically pulls the value for each corresponding k into the heap.
def largest(dictionary,numberWanted):
    return heapq.nlargest(numberWanted, dictionary, key = lambda k: dictionary[k])

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
        return(key, largest)
    
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
        biggestAmount = 0
        biggestRow = 0
        rowNum = 0
        workingFile = temp.readlines()
        table = []
        for line in workingFile:
            table.append(line.split(","))
        for row in table[1:]:
            rowNum = rowNum + 1
            toInt = row[colNum][1:].rstrip("\n")
            if (int(toInt[:-3]) > biggestAmount):
                biggestAmount = int(toInt[:-3])
                biggestRow = rowNum
        print("The Best Customer is: ", table[biggestRow][1],table[biggestRow][2])
        print("They have paid: ", biggestAmount)
        print("$" * (int(float(biggestAmount)/100)))
        print("Each '$' = 100 dollars")
        print("Their IP Address indicates they are located in", IPQuery(table[biggestRow][5])[5])

#This function takes an IP address and feeds it into a geolocation API, it returns a list of location data.
#Uses API described here: http://ip-api.com/docs/
def IPQuery(ip_address):
    serviceurl = 'http://ip-api.com/csv/'
    url = serviceurl + ip_address
    uh = urllib.request.urlopen(url)
    result = uh.read().decode()
    line = result.split(",")
    resultingList = []
    for item in line:
        if item == "":
            resultingList.append("no value")
        else:
            resultingList.append(item)
            
    return(resultingList)
   
    