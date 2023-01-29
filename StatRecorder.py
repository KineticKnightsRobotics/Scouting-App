# David Ertel
# 1/18/23
# StatRecorder

import os, time# imports the os module and system module

canRun = True # a boolean that controls whether the main loop can run
picking = True # if the user is picking not

def accessMode(mode, L): # this allows the user to change the data in the table
    picking = True
    
    if type(L[mode]) == int: # if the element is an integer
        while picking:
            userinput = input('enter an integer: ')

            if userinput.isdigit():
                L[mode] = int(userinput)
                picking = False

            else:
                print('try an integer')
                time.sleep(2)
                os.system('cls') # cls
                
    if type(L[mode]) == float: # if the element is a float
        while picking:
            userinput = input('enter a time (in decimal format): ')

            if userinput.isdigit():
                L[mode] = float(userinput)
                picking = False

            else:
                print('try a number')
                time.sleep(2)
                os.system('cls') # cls
   
    elif type(L[mode]) == list: # if the element is a list
        for k in range(3):
            while picking:
                userinput = input('enter an integer ('+ str(k) + ' of 3): ')

                if userinput.isdigit():
                    L[mode][k] = int(userinput)
                    picking = False
                else:
                    print('try an integer')
                    time.sleep(2) # waits 2 seconds
                    os.system('cls') # cls

            picking = True
                           
    else: # if the element is a string
        while picking:
            userinput = input('enter y if true or n if false: ')

            if userinput == 'y':
                L[mode] = "True"
                picking = False
                
            elif userinput == 'n':
                L[mode] = "False"
                picking = False

            else: # if the input is not y or n
                print('try y or n')
                time.sleep(2)
                os.system('cls') # cls
                
                
    print(L) # prints the entire table at the end    
    time.sleep(2)
    
def fileMenu(L): # main program
    # init variables
    chooseMode = True
    cnt = 0 # a counting variable for numbering the
    names = ['community', 'scoring', 'docking', 'links', 'cycleTime'] # stores the names of the options
    
    while chooseMode: # this is the main program loop for editing data while the match is going on
        print('Which stat would you like to access?')
        
        for i in L:
            print('> [' + str(cnt) + '] ' + names[cnt] + '\n')
            cnt += 1 # counts the array position of the element
            
        cnt = 0 # resets the count value
        
        userinput = input('Enter the corresponding number to change. type "save" to save data: \n>')
        userinput = userinput.lower() # lowers all of the input

        # if statement mess
        
        if userinput == 'save':
            chooseMode = False
            
        elif userinput.isdigit():
            if int(userinput) < len(L):
                
                accessMode(int(userinput), L)
        else:
            print('input is not acceptable. Try again')
            time.sleep(2)

        os.system('cls') # cls

def makeFile(pDir, L): # makes the file
    
    with open(os.path.join(pDir, 'teamTable.txt'), 'w') as file: # makes and opens the file

        for i in L:
            if type(i) == list:
                for k in i:
                    file.write(str(k) + '\n')
            else:
                file.write(str(i) + '\n')

        file.close()
        
def makeFolder(pDir): # declaring a function to make a folder
    os.mkdir(pDir) # makes the new directory
    
    # inits values for next folder
    
    inCommunity = "false"
    scoring = [0, 0, 0]
    docking = [0, 0, 0]
    links = 0
    cycleTime = 0.0
    
    L = [inCommunity, scoring, docking, links, cycleTime] # a list of a bunch of data
    
    # runs the file editing functions
    
    fileMenu(L) # brings up the file editing menu
    makeFile(pDir, L) # actually makes the file

def countFoldersWithSameName(n): # this function counts how many folders have the same name inputted that are in the same directory
    
    cnt = 0 # counts how many times the for loop iterates
    nameCnt = 0 # counts howmany files are named the same
    ltrCnt = 1 # counts letters in file names. Starts at 1 because the lowest amount of characters a string with one letter in it is one
    synthesizedString = "" # represents the files name re-constructed
    
    for path in os.walk(os.getcwd()): # prints out the entire directory including what is inside folders
        
        if cnt < 1: # the objects in the base path 
            print(path[1]) # prints out the array
            
            for f in path[1]: # iterates through the files in the path
                
                for letter in f: # iterates through the letters in the filename
                    if ltrCnt <= len(n): # iterates until the synthesized filename is as long as the proposed filename
                       
                        synthesizedString += letter # adds a character to the synthesized filename
                        
                        ltrCnt += 1
                        
                if synthesizedString == n: # if the name of the file is the same as the proposed filename 
                    nameCnt += 1

                synthesizedString = "" # resets the synthesized filename and the letter counting variable
                ltrCnt = 1
                
            cnt += 1 # stops the for loop from iterating through garbage I don't need right now
             
        else: # if cnt > 1
            break # breaks the loop

    return nameCnt + 1 # will return the amount of folders with the same name as the proposed folder plus one because the proposed folder isn't made yet

def chooseMakeFolder(p, c):
     while p: # this loop runs until a decision is made
        newVar = "New folder: " + proposedDir + " created. Do you want to make another? (y/n):"
        userInput = input(newVar) # stores the user's choice in a variable

        userInput.lower() # lowercases all input

        if userInput == "n": # if the user enters "n"
            c = False # stops the main loop from running
            p = False # stops the picking loop
            return p, c # returns p and c as false
        
        elif userInput == "y": # if the user enters "y"
            p = False # just stops the picking loop because the user wants to make another folder
            return p, c # returns p as false and c as true
    
        else: # if the user didn't enter a vaild response
            print("not valid response, try y or n")
                
# will run repeatedly

# MAIN ############################################################################################################################################################

while canRun:
    
    folderName = input("please input the name of a folder you want to make: ") # prompts the user to make a new file
    proposedDir = str(os.getcwd() + "/" + folderName) # saves the proposed directory of the file in a variable

    if not os.path.exists(proposedDir): # if there is no folder with the proposed name already
        makeFolder(proposedDir) # makes the new directory
        
        picking, canRun = chooseMakeFolder(picking, canRun) # the user decides if they want to make another file or exit the program
        
    else: # if there is already a folder with the same name as the proposed name
        
        while picking: # this loop runs until a decision is made
            newVar = "There is already a folder with the name: " + folderName + " in the directory: " + os.getcwd() + " Do you wish to proceed? : "
            userInput = input(newVar) # stores the user's choice in a variable
            
            userInput.lower() # lowercases all input
        
            if userInput == "n": # if the user enters "n"
                
                picking = False # stops the picking loop
                
            elif userInput == "y": # if the user enters "y"
                
                makeFolder(proposedDir + "(" + str(countFoldersWithSameName(folderName)) + ")") # makes a folder with extra numbers to separate it from like-named folders
               
                picking, canRun = chooseMakeFolder(picking, canRun) # the user decides if they want to make another file or exit the program
                
            else: # if the user didn't enter a vaild response
                print("not valid response, try y or n")
                
    picking = True # the next time the user picks to make a new file, the picking loop will run until they pick a vaild option

    # When the file is created or not, the shell clears after 3 seconds
    
    os.system('cls') # clears the screen
