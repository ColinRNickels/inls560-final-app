#!usr/bin/python3
userWantsToKeepGoing = True
while(userWantsToKeepGoing):
    userSays = str(input("Do you want to keep going \n"))
    print((userSays == "no"))
    if(userSays == "no"):
        userWantsToKeepGoing = False
    else:
        input("how about now?")
