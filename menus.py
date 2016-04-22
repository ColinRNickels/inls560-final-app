#!usr/bin/python3
# This is where we host our functions that display menus
from variables import *
from fileChangers import *

def fileMenu():
    print(optionsFiles)
    going = True
    while(going):
        userSays = input("Please select one of the above options \n")
        if(userSays == "5"):
            sys.exit()
        elif(userSays == "1"):
            print("you said 1")
            fileOpen = "mock_data1.csv"
            fileOptions(fileOpen)
        elif(userSays == "2"):
            print("you said 2")
            fileOpen = "mock_data2.csv"
            fileOptions(fileOpen)
        elif(userSays == "3"):
            print("you said 3")
            fileOpen = "mock_data3.csv"
            fileOptions(fileOpen)
        elif(userSays == "4"):
            print("To import your own data, please go to the github repository and attach a file. \n Then come back here and rerun this program. \n If you've already done this, please give me the name of your file")
            fileOpen = input("")
            fileOptions(fileOpen)
        else:
            print("Please choose one of the options: " + optionsFiles)
            continue
            
            

def topLevelMenu():
    print(optionsTop)
    going = True
    while(going):
        userSays = input("Please select one of the above options \n")
        if(userSays == "3"):
            going = False
        elif(userSays == "1"):
            thing = openFile(fileMenu())
            print(thing)
        elif(userSays == "2"):
            print("To import your own data, please go to the github repository and attach a file. \n Then come back here and rerun this program. \n If you've already done this, please give me the name of your file")
            fileOptions(fileOpen)
            
def fileOptions(tarFile):
    print(optionsFunctions)
    going = True
    while (going):
        userSays = input("Please select one of the above options \n")
        if(userSays == "9"):
            break
        elif(userSays == "1"):
            percentBreakdown(tarFile, 4)
        else:
            print("Please choose on of the options: " + optionsFunctions)