#!usr/bin/python3
# This is where we host our functions that display menus
from menuText import *
from fileChangers import *

def fileMenu():
    going = True
    while(going):
        print("=" * 45)
        userSays = input("Please select one of the following options \n" + "=" * 45 + "\n" + optionsFiles  + "\n")
        if(userSays == "5"):
            break
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
            try: 
                with open(fileOpen) as f:
                    f.read()
            except:
                print("I don't recognize that file")
                continue
            fileOptions(fileOpen)
        if(userSays == "x"):
            #Found this way to exit on http://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used
            raise SystemExit()
        if(userSays == "?"):
            print(helpText)
        
        else:
            continue
            
            

def topLevelMenu():
    going = True
    while(going):
        print("=" * 45)
        userSays = input("Please select one of the following options \n"  + "=" * 45 + "\n" + optionsTop + "\n")
        if(userSays == "x"):
            going = False
        elif(userSays == "1"):
            thing = openFile(fileMenu())
            print(thing)
        elif(userSays == "2"):
            print("To import your own data, please go to the github repository and attach a file. \n Then come back here and rerun this program. \n If you've already done this, please give me the name of your file")
            fileToOpen = input("What is the name of your data file \n")
            try: 
                with open(fileToOpen) as f:
                    f.read()
            except:
                print("I don't recognize that file")
                continue
            fileOptions(fileToOpen)
        elif(userSays == "?"):
            print(helpText)
        else: 
            continue
            
def fileOptions(tarFile):
    going = True
    while (going):
        print("=" * 45)
        userSays = input("Please select one of the following options \n" + "=" * 45 + "\n" + optionsFunctions + "\n")
        if(userSays == "9"):
            going = False
        
        if(userSays == "x"):
            #Found this way to exit on http://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used
            raise SystemExit()
            
        elif(userSays == "1"):
            percentBreakdown(tarFile, 4)
            going = askContinue()
            
        elif(userSays == "2"):
            topFive(tarFile, 1)
            going = askContinue()
           
        elif(userSays == "3"):
            topFive(tarFile, 2)
            going = askContinue()
            
        elif(userSays == "4"):
            print("The average amount owed is: ", averageValue(tarFile, 7))
            going = askContinue()
            
        elif(userSays == "5"):
            print("The average amount paid is: ", averageValue(tarFile, 8))
            
            going = askContinue()
            
        elif(userSays == "6"):
            bDomain, numRefs = number1(tarFile, 6)
            print("The best referring domain is:",bDomain)
            print("With " + str(numRefs) + " refferals")
            going = askContinue()
            
        elif(userSays == "7"):
            topCustomer(tarFile,8)
            going = askContinue()
        
        elif(userSays == "8"):
            going = False
            
        elif(userSays == "?"):
            print(helpText)
            
        else:
           continue
       
def askContinue():
    going = True
    while(going):
        print("=" * 45)
        userSays = input("Please select one of the following options \n"  + "=" * 45 + "\n" + done + "\n")
        if(userSays == "x"):
            raise SystemExit
        elif(userSays == "1"):
            return True
        elif(userSays == "2"):
            return False
        elif(userSays == "?"):
            print(helpText)
        else:
            continue