#this is just messing around. Actual code will live in a different file

print ("hello world")
userWantsToKeepGoing = True
while(userWantsToKeepGoing):
    userSays = str(input("Do you want to keep going"))
    print(userSays)
    if(userSays == "no"):
        userWantsToKeepGoing = False
    else:
        input("how about now?")