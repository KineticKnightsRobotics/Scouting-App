# David Ertel
# 1/18/23
# StatRecorder

import os, time# imports the os module and system module

canRun = True # a boolean that controls whether the main loop can run
picking = True # if the user is picking not
Teams_Dir = str(os.getcwd() + '/TEAMS')

#########################################################################################

def accessMode(mode, L): # this allows the user to change the data in the table
    global picking
    picking = True
    
    if type(L[mode]) == int: # if the element is an integer
        while picking:
            userinput = input('enter an integer: ')
            userInput.lower() # lowercases all input
            
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
            userInput.lower() # lowercases all input
            
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
                userInput.lower() # lowercases all input
                
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
            userInput.lower() # lowercases all input
            
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

######################################################################################################################
    
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

######################################################################################################################

def makeFile(pDir, L, element): # makes the file
    fileName = 'teamTable' # saves the name of the data tables
    print(pDir)
    nameCnt = countFoldersWithSameName(fileName, pDir, element) # gets how many files are named the same as the current file
    
    with open(os.path.join(pDir, fileName + '(' + str(nameCnt) + ')'), 'w') as file: # makes and opens the file

        for i in L: # cycles through the data table
            if type(i) == list: # if the type of the data is a list, the list has to be iterated over in order to write the data (only strings can be written)
                for k in i:
                    file.write(str(k) + '\n') # writes to the file 
            else:
                file.write(str(i) + '\n') # writes to the file

        file.close() # closes the file

######################################################################################################################
        
def makeFolder(pDir, element): # declaring a function to make a folder
    
    if not os.path.exists(pDir): # if the path doesn't exist
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
    makeFile(pDir, L, element) # actually makes the file

######################################################################################################################

def countFoldersWithSameName(n, DIR, element): # this function counts how many folders have the same name inputted that are in the same directory
    
    cnt = 0 # counts how many times the for loop iterates
    nameCnt = 0 # counts howmany files are named the same
    ltrCnt = 1 # counts letters in file names. Starts at 1 because the lowest amount of characters a string with one letter in it is one
    synthesizedString = "" # represents the files name re-constructed
    
    for path in os.walk(DIR): # prints out the entire directory including what is inside folders
        
        if cnt < 1: # the objects in the base path 
            print(path[element]) # prints out the array
            
            for f in path[element]: # iterates through the files in the path
                
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

    return nameCnt # will return the amount of folders with the same name as the proposed folder plus one because the proposed folder isn't made yet

######################################################################################################################

def newFolder(): # this makes a new folder
    global picking
    global canRun
    
    folderName = input("please input the name of a folder you want to make: ") # prompts the user to make a new file
    proposedDir = str(Teams_Dir + "/" + folderName) # saves the proposed directory of the file in a variable

    if not os.path.exists(proposedDir): # if there is no folder with the proposed name already
        makeFolder(proposedDir, 1) # makes the new directory
        
        picking, canRun = chooseMakeFolder(picking, canRun, proposedDir) # the user decides if they want to make another file or exit the program
        
    else: # if there is already a folder with the same name as the proposed name
        
        while picking: # this loop runs until a decision is made
            newVar = "There is already a folder with the name: " + folderName + " in the directory: " + os.getcwd() + " Do you wish to proceed? : "
            userInput = input(newVar) # stores the user's choice in a variable
            
            userInput.lower() # lowercases all input
        
            if userInput == "n": # if the user enters "n"
                
                picking = False # stops the picking loop
                
            elif userInput == "y": # if the user enters "y"
                
                makeFolder(proposedDir + "(" + str(countFoldersWithSameName(folderName, Teams_Dir, 1)) + ")", 1) # makes a folder with extra numbers to separate it from like-named folders
               
                picking, canRun = chooseMakeFolder(picking, canRun, proposedDir) # the user decides if they want to make another file or exit the program
                
            else: # if the user didn't enter a vaild response
                print("not valid response, try y or n")

######################################################################################################################

def preExistingFolder():
    teamTable = []
    foundFolder = False
    
    global picking # references global variables before use
    global canRun
    
    picking = True
    
    for path in os.walk(Teams_Dir): # brings up a table that contains the path, folders, and files in the directory
        for team in path[1]:
            print('eeeeeee')
            teamTable.append(team) # appends the team

    if len(teamTable) > 0:        
        while picking: # prints out a list of the teams
            for team in teamTable:
                print('> ', team)
                
            folderName = input('What team do you want to add to?: \n') # prompts the user to choose which file to add to
            
            for team in teamTable: # checks if the team exists
                if folderName == str(team):
                    foundFolder = True
                    picking = False
                    proposedDir = str(Teams_Dir + "/" + folderName) # saves the proposed directory of the file in a variable
                    break # breaks the loop
                
            if not foundFolder:
                print('Could not find the folder. Try again')
                time.sleep(2)
                os.system('cls') # clears the screen
            
        os.system('cls') # clears the screen
        picking = True

        makeFolder(proposedDir, 2) # makes the new directory
            
        picking, canRun = chooseMakeFolder(picking, canRun, proposedDir) # the user decides if they want to make another file or exit the program

        # resets some variables
        teamTable = []
        foundFolder = False
    else:
        print('No folders found.')

######################################################################################################################
def chooseMakeFolder(p, c, proposedDir):
    
    p = True # inits picking as true
    
    while p: # this loop runs until a decision is made
        newVar = "New folder: " + proposedDir + " created. Do you want to make another? (y/n):"
        userInput = input(newVar) # stores the user's choice in a variable

        userInput.lower() # lowercases all input

        if userInput == "n": # if the user enters "n"
            print('e')
            c = False # stops the main loop from running
            p = False # stops the picking loop
            return p, c # returns p and c as false
        
        elif userInput == "y": # if the user enters "y"
            print('r')
            p = False # just stops the picking loop because the user wants to make another folder
            
            return p, c # returns p as false and c as true
    
        else: # if the user didn't enter a vaild response
            print("not valid response, try y or n")
            
# MAIN ############################################################################################################################################################

while canRun: # will run repeatedly

    # loop for choosing where the file will go
    while picking:
        userInput = input("Would you like to make a file in a new folder or in a pre-existing folder (n/p):\n") # prompts the user to either make a new file or make a file in an already made one
        userInput.lower() # lowercases all input

        # if the input entered is not n or p
        if not userInput == 'n' and not userInput == 'p':
            print('Try "n" or "p".')
            time.sleep(2)
            os.system('cls') # clears the screen

        # if the input is acceptable
        else:
            picking = False
            os.system('cls') # clears the screen

    picking = True # resets the boolean for its next use
    
    if userInput == 'n': # if a new folder is to be made
        newFolder() # makes a new folder and makes a new file
                    
    elif userInput == 'p': # if people want to be boring and put more files into one folder
        preExistingFolder() # just makes a new file, not a new folder
    
    picking = True # the next time the user picks to make a new file, the picking loop will run until they pick a vaild option

    # When the file is created or not, the shell clears after 1 seconds
    time.sleep(1)
    os.system('cls') # clears the screen
